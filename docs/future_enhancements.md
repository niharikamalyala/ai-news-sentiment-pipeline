# Future Enhancements

## Planned Improvements

- Replace rule-based sentiment analysis with an LLM or transformer model (e.g., BERT).
- Consume live news streams instead of processing sample JSON files.
- Integrate AWS Glue Data Catalog for metadata management.
- Add Apache Iceberg or Delta Lake support for ACID transactions.
- Deploy the pipeline using Kubernetes.
- Add Prometheus and Grafana dashboards for monitoring.
- Integrate Slack or email notifications for pipeline failures.
- Add schema evolution support.
- Add data lineage using OpenLineage or Marquez.
- Expand automated unit and integration test coverage.

## Current Limitations

- Uses a sample dataset for demonstration.
- Assumes a single Kafka broker.
- Uses basic keyword-based sentiment analysis.
- Does not include authentication for external APIs beyond API keys.
- Dashboard implementation is outside the current project scope.
