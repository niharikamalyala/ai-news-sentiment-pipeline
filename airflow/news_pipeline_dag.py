from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="ai_news_sentiment_pipeline",
    description="Orchestrates the AI-powered news sentiment data pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["news", "data-engineering", "sentiment"],
) as dag:

    ingest_news = BashOperator(
        task_id="ingest_news",
        bash_command="python pyspark/ingest_news.py",
    )

    publish_to_kafka = BashOperator(
        task_id="publish_to_kafka",
        bash_command="python kafka/producer.py",
    )

    process_news = BashOperator(
        task_id="process_news",
        bash_command="python pyspark/process_news.py",
    )

    ingest_news >> publish_to_kafka >> process_news
