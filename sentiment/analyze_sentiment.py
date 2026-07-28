from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat_ws, lower, when


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
    return (
        SparkSession.builder
        .appName("NewsSentimentAnalysis")
        .getOrCreate()
    )


def analyze_sentiment() -> None:
    spark = create_spark_session()

    input_path = "data/processed/news_articles"
    output_path = "data/curated/news_sentiment"

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
        when(positive_condition & ~negative_condition, "positive")
        .when(negative_condition & ~positive_condition, "negative")
        .otherwise("neutral"),
    )

    Path("data/curated").mkdir(parents=True, exist_ok=True)

    sentiment_df.write.mode("overwrite").parquet(output_path)

    print(f"Analyzed sentiment for {sentiment_df.count()} articles.")

    spark.stop()


if __name__ == "__main__":
    analyze_sentiment()
