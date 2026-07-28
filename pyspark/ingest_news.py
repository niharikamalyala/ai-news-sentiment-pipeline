import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from configs.config import CATEGORY, COUNTRY, NEWS_API_URL, PAGE_SIZE
from utils.logger import logger


load_dotenv()


def fetch_news() -> dict:
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        raise ValueError("NEWS_API_KEY is not configured.")

    params = {
        "apiKey": api_key,
        "country": COUNTRY,
        "category": CATEGORY,
        "pageSize": PAGE_SIZE,
    }

    response = requests.get(
        NEWS_API_URL,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def save_raw_news(news_data: dict) -> None:
    output_path = Path("data/raw/news_articles.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            news_data,
            file,
            indent=2,
            ensure_ascii=False,
        )

    logger.info(
        "Raw news data saved to %s.",
        output_path,
    )


def main() -> None:
    logger.info("Starting News API ingestion.")

    try:
        news_data = fetch_news()
        save_raw_news(news_data)

        article_count = len(news_data.get("articles", []))

        logger.info(
            "Successfully collected %s news articles.",
            article_count,
        )

    except requests.RequestException as error:
        logger.exception(
            "News API request failed: %s",
            error,
        )
        raise

    except Exception as error:
        logger.exception(
            "News ingestion failed: %s",
            error,
        )
        raise


if __name__ == "__main__":
    main()
