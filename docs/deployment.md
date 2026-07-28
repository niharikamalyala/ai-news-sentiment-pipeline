# Deployment Guide

## Deployment Architecture

- News API
- Apache Kafka
- Apache Airflow
- PySpark
- Amazon S3
- Amazon Redshift

## Deployment Steps

### 1. Create AWS Resources

- Amazon S3 Bucket
- Amazon Redshift Cluster
- IAM Role
- CloudWatch Logs

### 2. Configure Environment Variables

Populate the following values in your `.env` file:

- NEWS_API_KEY
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- S3_BUCKET_NAME
- REDSHIFT_HOST
- REDSHIFT_PORT
- REDSHIFT_DATABASE
- REDSHIFT_USER
- REDSHIFT_PASSWORD
- REDSHIFT_IAM_ROLE

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Kafka

```bash
docker compose up -d
```

### 5. Run the Pipeline

```bash
python pyspark/ingest_news.py
python kafka/producer.py
python pyspark/process_news.py
python sentiment/analyze_sentiment.py
python aws/upload_to_s3.py
python aws/load_to_redshift.py
```

### 6. Production Recommendations

- Store secrets in AWS Secrets Manager.
- Schedule workflows using Apache Airflow.
- Monitor logs with Amazon CloudWatch.
- Configure alerts for pipeline failures.
- Use IAM roles instead of long-lived AWS access keys.
