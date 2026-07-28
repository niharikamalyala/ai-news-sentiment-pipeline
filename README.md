![Python](https://img.shields.io/badge/Python-3.11-blue)
![PySpark](https://img.shields.io/badge/PySpark-ETL-orange)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-green)
![AWS](https://img.shields.io/badge/AWS-Cloud-yellow)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-success)
![License](https://img.shields.io/badge/License-MIT-brightgreen)


# AI-Powered News Sentiment Data Pipeline

## Overview

This project demonstrates an end-to-end data engineering pipeline that collects news articles from external APIs, processes the data using Python and PySpark, performs sentiment analysis, and produces analytics-ready datasets.

The project is designed to demonstrate practical data engineering concepts such as API ingestion, batch and streaming processing, data transformation, workflow orchestration, data quality, data lake storage, and analytical reporting.

## Business Problem

Organizations receive large volumes of news data from multiple publishers every day. Manually reviewing this information is time-consuming and makes it difficult to identify public sentiment, important topics, and emerging trends.

This pipeline automates the collection and processing of news articles and classifies the sentiment of each article as positive, negative, or neutral.

## Planned Architecture

```text
News API
   |
   v
Python Ingestion
   |
   v
Apache Kafka
   |
   v
Spark Structured Streaming
   |
   v
Sentiment Analysis
   |
   v
AWS S3 Data Lake
   |
   v
AWS Glue Data Catalog
   |
   v
Amazon Redshift
   |
   v
Power BI
```

## Technology Stack

- Python
- PySpark
- Apache Spark
- Apache Kafka
- Apache Airflow
- REST APIs
- AWS S3
- AWS Glue
- Amazon Redshift
- SQL
- Docker
- GitHub Actions

## Key Features

- News article ingestion through REST APIs
- Batch and streaming data processing
- PySpark-based cleansing and transformation
- AI-powered sentiment classification
- Bronze, Silver, and Gold data lake layers
- Workflow orchestration using Apache Airflow
- Data-quality validation and error handling
- Analytics-ready SQL datasets
- Cloud deployment using AWS services

## Repository Structure

```text
ai-news-sentiment-pipeline/
├── architecture/
├── airflow/
├── kafka/
├── pyspark/
├── sql/
├── configs/
├── sample_data/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

## Project Status

This project is currently under active development.

## Author

**Niharika Malyala**

Data Engineer

- Python
- SQL
- PySpark
- Apache Spark
- AWS
- Azure
- Apache Kafka
- Apache Airflow

---

# Project Workflow

1. Extract news articles from News API.
2. Publish news events to Apache Kafka.
3. Consume events from Kafka.
4. Transform and clean the data using PySpark.
5. Validate processed data.
6. Perform sentiment analysis.
7. Store curated data in Amazon S3.
8. Load curated data into Amazon Redshift.
9. Orchestrate the workflow using Apache Airflow.
10. Monitor the pipeline using centralized logging and GitHub Actions.

---

# Technology Stack

- Python
- Apache Kafka
- Apache Airflow
- Apache Spark (PySpark)
- Amazon S3
- Amazon Redshift
- Docker
- Docker Compose
- GitHub Actions
- Pytest

---

# Repository Structure

```text
airflow/
architecture/
aws/
configs/
data/
docs/
kafka/
pyspark/
sentiment/
tests/
utils/
validation/
```
