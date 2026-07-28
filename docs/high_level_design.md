# High Level Design (HLD)

## Objective

Build a scalable, cloud-native data engineering pipeline that ingests news articles, processes them, performs sentiment analysis, and stores analytics-ready datasets.

---

## Architecture Components

### Data Source
- News API

### Data Ingestion
- Python
- REST API

### Streaming Layer
- Apache Kafka

### Processing Layer
- Apache Spark (PySpark)

### Data Quality
- Validation Module

### Analytics Layer
- Sentiment Analysis

### Storage Layer
- Amazon S3

### Data Warehouse
- Amazon Redshift

### Orchestration
- Apache Airflow

### Monitoring
- Centralized Logging

### CI/CD
- GitHub Actions

### Containerization
- Docker
- Docker Compose

---

## Non-Functional Requirements

- Scalability
- Fault Tolerance
- Data Validation
- Centralized Logging
- Modular Design
- Automated Testing
- Cloud Ready
