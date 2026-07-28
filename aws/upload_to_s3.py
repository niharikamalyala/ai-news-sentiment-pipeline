import os
from pathlib import Path

import boto3
from dotenv import load_dotenv


load_dotenv()

S3_BUCKET = os.getenv("S3_BUCKET_NAME")
LOCAL_FILE = Path("data/raw/sample_news.json")
S3_KEY = "raw/sample_news.json"


def upload_file_to_s3() -> None:
    if not S3_BUCKET:
        raise ValueError("S3_BUCKET_NAME is not configured.")

    if not LOCAL_FILE.exists():
        raise FileNotFoundError(f"File not found: {LOCAL_FILE}")

    s3_client = boto3.client("s3")

    s3_client.upload_file(
        str(LOCAL_FILE),
        S3_BUCKET,
        S3_KEY,
    )

    print(
        f"Successfully uploaded {LOCAL_FILE} "
        f"to s3://{S3_BUCKET}/{S3_KEY}"
    )


if __name__ == "__main__":
    upload_file_to_s3()
