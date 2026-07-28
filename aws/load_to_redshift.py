import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.getenv("REDSHIFT_HOST"),
        port=os.getenv("REDSHIFT_PORT"),
        database=os.getenv("REDSHIFT_DATABASE"),
        user=os.getenv("REDSHIFT_USER"),
        password=os.getenv("REDSHIFT_PASSWORD"),
    )


def load_curated_data():
    connection = get_connection()
    cursor = connection.cursor()

    copy_command = f"""
    COPY news_sentiment
    FROM 's3://{os.getenv("S3_BUCKET_NAME")}/curated/news_sentiment/'
    IAM_ROLE '{os.getenv("REDSHIFT_IAM_ROLE")}'
    FORMAT AS PARQUET;
    """

    cursor.execute(copy_command)
    connection.commit()

    print("Successfully loaded curated data into Amazon Redshift.")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    load_curated_data()
