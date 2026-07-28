# Local Setup Guide

## Prerequisites

- Python 3.11+
- Apache Kafka
- Apache Spark
- Docker
- Docker Compose
- Git

## Clone Repository

```bash
git clone https://github.com/<your-github-username>/ai-news-sentiment-pipeline.git
cd ai-news-sentiment-pipeline
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Update `.env` with your:

- News API key
- AWS credentials
- Amazon Redshift connection details
- S3 bucket name

## Start Kafka

```bash
docker compose up -d
```

## Run the Pipeline

```bash
python pyspark/ingest_news.py
python kafka/producer.py
python pyspark/process_news.py
python sentiment/analyze_sentiment.py
```

## Run Tests

```bash
pytest
```
