# Airflow Module

This module contains Apache Airflow DAGs used to orchestrate the news sentiment data pipeline.

## Planned Workflow

1. Extract news articles from the News API
2. Publish articles to Kafka
3. Process articles using PySpark
4. Store processed data
5. Run sentiment analysis
6. Load curated data for analytics
