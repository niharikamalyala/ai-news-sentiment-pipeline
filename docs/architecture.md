# AI-Powered News Sentiment Data Pipeline

## Architecture

```text
                 +----------------------+
                 |     News API         |
                 +----------+-----------+
                            |
                            v
                  Python Ingestion Script
                            |
                            v
                     Apache Kafka Topic
                            |
                            v
                    Kafka Consumer
                            |
                            v
                  PySpark Processing
                            |
                            v
                  Data Validation Layer
                            |
                            v
                  Sentiment Analysis
                            |
                            v
                     Amazon S3 Data Lake
                            |
                            v
                  Amazon Redshift Warehouse
                            |
                            v
                    Power BI Dashboard
```

## Orchestration

Apache Airflow orchestrates the entire workflow.

## Monitoring

- Centralized Logging
- GitHub Actions CI
- Docker
- Docker Compose
