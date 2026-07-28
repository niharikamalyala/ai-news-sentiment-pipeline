import json
import time
from pathlib import Path

from kafka import KafkaProducer

from utils.logger import logger


KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "news-articles"
INPUT_FILE = Path("data/raw/sample_news.json")


def create_producer() -> KafkaProducer:
    logger.info(
        "Connecting Kafka producer to broker %s.",
        KAFKA_BROKER,
    )

    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda value: json.dumps(value).encode(
            "utf-8"
        ),
    )


def load_articles() -> list[dict]:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    with INPUT_FILE.open("r", encoding="utf-8") as file:
        news_data = json.load(file)

    articles = news_data.get("articles", [])

    logger.info(
        "Loaded %s articles from %s.",
        len(articles),
        INPUT_FILE,
    )

    return articles


def publish_articles() -> None:
    producer = None

    try:
        logger.info("Starting Kafka news producer.")

        producer = create_producer()
        articles = load_articles()

        for article in articles:
            title = article.get("title", "Unknown title")

            producer.send(
                KAFKA_TOPIC,
                value=article,
            )

            logger.info(
                "Published article to topic %s: %s",
                KAFKA_TOPIC,
                title,
            )

            time.sleep(1)

        producer.flush()

        logger.info(
            "Successfully published %s articles.",
            len(articles),
        )

    except Exception as error:
        logger.exception(
            "Kafka producer failed: %s",
            error,
        )
        raise

    finally:
        if producer is not None:
            producer.close()
            logger.info("Kafka producer closed.")


if __name__ == "__main__":
    publish_articles()
