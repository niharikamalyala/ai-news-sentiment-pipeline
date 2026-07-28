from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from utils.logger import logger


REQUIRED_COLUMNS = [
    "source_name",
    "title",
    "url",
    "published_at",
    "content",
]


def create_spark_session() -> SparkSession:
    return (
        SparkSession.builder
        .appName("NewsDataValidation")
        .getOrCreate()
    )


def validate_news_data() -> None:
    spark = None

    try:
        logger.info("Starting processed news data validation.")

        spark = create_spark_session()

        input_path = "data/processed/news_articles"
        news_df = spark.read.parquet(input_path)

        missing_columns = [
            column
            for column in REQUIRED_COLUMNS
            if column not in news_df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        null_condition = None

        for column in REQUIRED_COLUMNS:
            condition = col(column).isNull()

            null_condition = (
                condition
                if null_condition is None
                else null_condition | condition
            )

        invalid_count = news_df.filter(null_condition).count()
        total_count = news_df.count()

        if total_count == 0:
            raise ValueError("Processed news dataset is empty.")

        if invalid_count > 0:
            raise ValueError(
                f"Validation failed: {invalid_count} invalid records found."
            )

        logger.info(
            "Validation passed for %s processed news records.",
            total_count,
        )

    except Exception as error:
        logger.exception(
            "News data validation failed: %s",
            error,
        )
        raise

    finally:
        if spark is not None:
            spark.stop()
            logger.info("Spark session stopped.")


if __name__ == "__main__":
    validate_news_data()
