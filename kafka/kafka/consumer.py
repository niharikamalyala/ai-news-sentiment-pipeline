import json

from kafka import KafkaConsumer

from utils.logger import logger


KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "news-articles"
CONSUMER_GROUP = "news-sentiment-group"


def create_consumer() -> KafkaConsumer:
    logger.info(
        "Connecting Kafka consumer to broker %s.",
        KAFKA_BROKER,
    )

    return KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BROKER,
        group_id=CONSUMER_GROUP,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda message: json.loads(
            message.decode("utf-8")
        ),
    )


def consume_articles() -> None:
    consumer = None

    try:
        logger.info(
            "Starting Kafka consumer for topic %s.",
            KAFKA_TOPIC,
        )

        consumer = create_consumer()

        for message in consumer:
            article = message.value
            title = article.get("title", "Unknown title")

            logger.info(
                "Received article from partition %s at offset %s: %s",
                message.partition,
                message.offset,
                title,
            )

    except KeyboardInterrupt:
        logger.info("Kafka consumer stopped by the user.")

    except Exception as error:
        logger.exception(
            "Kafka consumer failed: %s",
            error,
        )
        raise

    finally:
        if consumer is not None:
            consumer.close()
            logger.info("Kafka consumer closed.")


if __name__ == "__main__":
    consume_articles()
