from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat_ws, lower, when

from utils.logger import logger


POSITIVE_WORDS = [
    "growth",
    "gain",
    "improve",
    "success",
    "strong",
    "increase",
    "positive",
]

NEGATIVE_WORDS = [
    "decline",
    "loss",
    "weak",
    "drop",
    "negative",
    "fall",
    "risk",
]


def create_spark_session() -> SparkSession:
    logger.info("Creating Spark session for sentiment analysis.")

    return (
        SparkSession.builder
        .appName("NewsSentimentAnalysis")
        .getOrCreate()
    )


def analyze_sentiment() -> None:
    spark = None

    try:
        logger.info("Starting news sentiment analysis.")

        spark = create_spark_session()

        input_path = "data/processed/news_articles"
        output_path = "data/curated/news_sentiment"

        logger.info(
            "Reading processed news data from %s.",
            input_path,
        )

        news_df = spark.read.parquet(input_path)

        text_column = lower(
            concat_ws(
                " ",
                col("title"),
                col("description"),
                col("content"),
            )
        )

        positive_condition = None

        for word in POSITIVE_WORDS:
            condition = text_column.contains(word)

            positive_condition = (
                condition
                if positive_condition is None
                else positive_condition | condition
            )

        negative_condition = None

        for word in NEGATIVE_WORDS:
            condition = text_column.contains(word)

            negative_condition = (
                condition
                if negative_condition is None
                else negative_condition | condition
            )

        sentiment_df = news_df.withColumn(
            "sentiment",
            when(
                positive_condition & ~negative_condition,
                "positive",
            )
            .when(
                negative_condition & ~positive_condition,
                "negative",
            )
            .otherwise("neutral"),
        )

        Path("data/curated").mkdir(
            parents=True,
            exist_ok=True,
        )

        sentiment_df.write.mode("overwrite").parquet(
            output_path
        )

        article_count = sentiment_df.count()

        logger.info(
            "Successfully analyzed sentiment for %s articles.",
            article_count,
        )

        logger.info(
            "Curated sentiment data saved to %s.",
            output_path,
        )

    except Exception as error:
        logger.exception(
            "Sentiment analysis failed: %s",
            error,
        )
        raise

    finally:
        if spark is not None:
            spark.stop()
            logger.info("Spark session stopped.")


if __name__ == "__main__":
    analyze_sentiment()
