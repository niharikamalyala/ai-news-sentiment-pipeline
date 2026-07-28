from configs.config import CATEGORY, COUNTRY, NEWS_API_URL, PAGE_SIZE


def test_news_api_url() -> None:
    assert NEWS_API_URL.startswith("https://")


def test_country_configuration() -> None:
    assert isinstance(COUNTRY, str)
    assert COUNTRY


def test_category_configuration() -> None:
    assert isinstance(CATEGORY, str)
    assert CATEGORY


def test_page_size_configuration() -> None:
    assert isinstance(PAGE_SIZE, int)
    assert PAGE_SIZE > 0
