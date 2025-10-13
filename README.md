# Reddit API Data Pipeline Project

**Status:** In Progress (Pipeline functional, visualizations in development)

---

## Overview

This project demonstrates a pipeline for extracting, transforming, and loading data from Reddit using the Reddit API. The dataset is stored in AWS Redshift and connected to Power BI for visualization and analysis.

> **Note:** This project was inspired by [ABZ-Aaron’s Reddit API Pipeline tutorial](https://github.com/ABZ-Aaron/reddit-api-pipeline/tree/master/instructions). I followed the tutorial to build the pipeline while applying my own understanding and modifications where applicable.

---

## Technologies Used

- **Python** (requests, pandas, etc.)
- **Reddit API** (PRAW)
- **AWS Services:**
  - **S3** – storing raw and processed data
  - **Redshift** – relational database for analytics
  - **IAM** – managing access and credentials
  - **boto3** – Python SDK for AWS integration
- **dbt** – data transformation
- **Power BI** – for initial data exploration
- **Airflow** – for orchestration
- **Docker** – for containerization
- **Terraform** – infrastructure as code
- **Git/GitHub** – version control

---

## Features Implemented

- Authenticated connection to Reddit API
- Data extraction and transformation for posts and comments
- Loading data into AWS Redshift
- Data transformation using dbt
- Initial connection to Power BI for data exploration
- Orchestration with Airflow in Docker
- Infrastructure setup with Terraform

*Note: Power BI visualizations are currently in progress.*

---

## Challenges & Learnings

- Successfully built the ETL pipeline, handling API authentication, AWS integration, and data storage.
- Implemented data transformations using dbt, enhancing data quality and consistency.
- Connected the dataset to Power BI, learning the initial setup process; advanced visualizations are still a work in progress.
- Gained experience in orchestrating workflows with Airflow and managing infrastructure with Terraform.

---

## Next Steps

- Develop interactive dashboards and visualizations in Power BI.
- Automate ETL updates to Redshift using scheduled scripts.
- Explore additional data insights and analytics from Reddit posts and comments.
- Optimize AWS S3/Redshift architecture for efficiency and cost.
- Enhance Airflow DAGs for better workflow management.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/reddit-api-pipeline.git
