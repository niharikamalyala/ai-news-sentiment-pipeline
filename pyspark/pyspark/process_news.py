from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    current_timestamp,
    lower,
    to_timestamp,
    trim,
)


def create_spark_session() -> SparkSession:
    return (
        SparkSession.builder
        .appName("NewsDataProcessing")
        .getOrCreate()
    )


def process_news() -> None:
    spark = create_spark_session()

    input_path = "data/raw/sample_news.json"
    output_path = "data/processed/news_articles"

    news_df = (
        spark.read
        .option("multiline", "true")
        .json(input_path)
    )

    articles_df = news_df.selectExpr("explode(articles) AS article")

    processed_df = articles_df.select(
        col("article.source.name").alias("source_name"),
        trim(col("article.author")).alias("author"),
        trim(col("article.title")).alias("title"),
        trim(col("article.description")).alias("description"),
        col("article.url").alias("url"),
        to_timestamp(col("article.publishedAt")).alias("published_at"),
        lower(trim(col("article.content"))).alias("content"),
        current_timestamp().alias("processed_at"),
    )

    Path("data/processed").mkdir(parents=True, exist_ok=True)

    processed_df.write.mode("overwrite").parquet(output_path)

    print(f"Processed {processed_df.count()} news articles.")

    spark.stop()


if __name__ == "__main__":
    process_news()
