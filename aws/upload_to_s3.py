import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

from utils.logger import logger


load_dotenv()

S3_BUCKET = os.getenv("S3_BUCKET_NAME")
LOCAL_FILE = Path("data/raw/sample_news.json")
S3_KEY = "raw/sample_news.json"


def upload_file_to_s3() -> None:
    try:
        logger.info("Starting S3 upload.")

        if not S3_BUCKET:
            raise ValueError("S3_BUCKET_NAME is not configured.")

        if not LOCAL_FILE.exists():
            raise FileNotFoundError(
                f"File not found: {LOCAL_FILE}"
            )

        s3_client = boto3.client("s3")

        s3_client.upload_file(
            str(LOCAL_FILE),
            S3_BUCKET,
            S3_KEY,
        )

        logger.info(
            "Successfully uploaded %s to s3://%s/%s.",
            LOCAL_FILE,
            S3_BUCKET,
            S3_KEY,
        )

    except Exception as error:
        logger.exception(
            "S3 upload failed: %s",
            error,
        )
        raise


if __name__ == "__main__":
    upload_file_to_s3()
