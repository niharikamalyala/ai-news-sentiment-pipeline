# Data Quality Checks

This project validates processed news data before it is loaded into downstream systems.

## Validation Rules

- Required columns must exist.
- Required columns cannot contain NULL values.
- Dataset must not be empty.
- Invalid records fail the pipeline.

## Benefits

- Prevents bad data from reaching Amazon Redshift.
- Improves data reliability.
- Supports trustworthy analytics and reporting.
- Enables early detection of data quality issues.
