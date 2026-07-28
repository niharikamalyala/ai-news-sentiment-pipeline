import json
import time
from pathlib import Path

from kafka import KafkaProducer


KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "news-articles"
INPUT_FILE = Path("data/raw/sample_news.json")


def create_producer() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    )


def load_articles() -> list[dict]:
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        news_data = json.load(file)

    return news_data.get("articles", [])


def publish_articles() -> None:
    producer = create_producer()
    articles = load_articles()

    for article in articles:
        producer.send(KAFKA_TOPIC, value=article)
        print(f"Published article: {article.get('title')}")
        time.sleep(1)

    producer.flush()
    producer.close()

    print(f"Published {len(articles)} articles successfully.")


if __name__ == "__main__":
    publish_articles()
