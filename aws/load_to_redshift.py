import os

import psycopg2
from dotenv import load_dotenv

from utils.logger import logger


load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise ValueError(f"{name} is not configured.")

    return value


def get_connection():
    logger.info("Connecting to Amazon Redshift.")

    return psycopg2.connect(
        host=get_required_env("REDSHIFT_HOST"),
        port=get_required_env("REDSHIFT_PORT"),
        database=get_required_env("REDSHIFT_DATABASE"),
        user=get_required_env("REDSHIFT_USER"),
        password=get_required_env("REDSHIFT_PASSWORD"),
    )


def load_curated_data() -> None:
    connection = None
    cursor = None

    try:
        bucket_name = get_required_env("S3_BUCKET_NAME")
        iam_role = get_required_env("REDSHIFT_IAM_ROLE")

        connection = get_connection()
        cursor = connection.cursor()

        copy_command = f"""
        COPY news_sentiment
        FROM 's3://{bucket_name}/curated/news_sentiment/'
        IAM_ROLE '{iam_role}'
        FORMAT AS PARQUET;
        """

        logger.info("Starting curated data load into Redshift.")

        cursor.execute(copy_command)
        connection.commit()

        logger.info(
            "Successfully loaded curated sentiment data into Redshift."
        )

    except Exception as error:
        if connection is not None:
            connection.rollback()

        logger.exception(
            "Redshift data loading failed: %s",
            error,
        )
        raise

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
            logger.info("Redshift connection closed.")


if __name__ == "__main__":
    load_curated_data()
