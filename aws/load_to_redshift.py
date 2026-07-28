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


def main():
    connection = get_connection()
    cursor = connection.cursor()

    print("Successfully connected to Amazon Redshift.")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
