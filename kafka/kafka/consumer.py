import json

from kafka import KafkaConsumer


KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "news-articles"


def create_consumer() -> KafkaConsumer:
    return KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda message: json.loads(message.decode("utf-8")),
    )


def consume_articles() -> None:
    consumer = create_consumer()

    print("Waiting for news articles...\n")

    for message in consumer:
        article = message.value
        print(f"Received: {article.get('title')}")


if __name__ == "__main__":
    consume_articles()
