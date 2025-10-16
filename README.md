# Reddit API Data Pipeline Project

**Status:** ✅ Completed

---

## Overview

This project demonstrates a complete data pipeline for extracting, transforming, and loading data from Reddit using the Reddit API.  
The dataset is stored in AWS Redshift and visualized in Power BI to analyze Reddit activity trends and insights.

> **Note:** This project was inspired by [ABZ-Aaron’s Reddit API Pipeline tutorial](https://github.com/ABZ-Aaron/reddit-api-pipeline/tree/master/instructions).  
> I followed the tutorial to build the pipeline while applying my own understanding and modifications where applicable.

---

## Technologies Used

- **Python** – for data extraction and ETL (requests, pandas, boto3)
- **Reddit API (PRAW)** – to collect posts and comments
- **AWS Services:**
  - **S3** – raw and processed data storage
  - **Redshift** – data warehouse for analytics
  - **IAM** – for credential and access management
- **dbt Cloud** – for online SQL-based data transformations
- **Airflow (Docker)** – for ETL orchestration and automation
- **Power BI** – for visualization and reporting
- **Terraform** – infrastructure as code (reference)
- **Git/GitHub** – for version control and documentation

---

## Features Implemented

- Reddit API authentication and data extraction  
- ETL pipeline with Python for Reddit posts and comments  
- AWS S3 integration for raw and processed data layers  
- Data warehousing using Amazon Redshift  
- Data transformation logic managed through **dbt Cloud**  
- Airflow DAGs used to orchestrate the workflow in Docker  
- Power BI dashboard connected to Redshift for interactive analytics  

---

## Challenges & Learnings

- Navigating Reddit API limitations and pagination handling  
- Managing AWS IAM permissions for secure data access  
- Debugging Airflow connection issues during Docker deployment  
- Gaining hands-on experience with **dbt Cloud transformations**  
- Connecting Power BI directly to Redshift for real-time analytics  

---

## Next Steps

- Continue refining Power BI visualizations and layout design  
- Explore automation of ETL jobs through scheduled Airflow DAGs  
- Integrate CI/CD practices for version-controlled dbt models  
- Optimize AWS Redshift query performance and costs  

---

## 📊 Power BI Dashboard

The Power BI dashboard displays key Reddit insights derived from the data pipeline — including subreddit activity, top authors, and engagement metrics.

![Power BI Screenshot](images/powerbi_dashboard.png)

*(Sample data shown for privacy. Dashboard visuals represent the completed pipeline.)*

---

## 🧩 Airflow DAG Example

Example of the Airflow DAG orchestrating the ETL process:

![Airflow DAG](images/GraphAirflow.png)

*(Sensitive credentials and connection strings have been removed.)*

---

## Setup Overview

1. Clone this repository to your local environment.  
2. Install dependencies listed in `requirements.txt`.  
3. Configure Reddit API credentials in a local configuration file.  
4. Set up AWS resources (S3, Redshift, IAM) and connect via `boto3`.  
5. Run Python ETL scripts to extract and load Reddit data.  
6. Perform transformations using dbt Cloud.  
7. Connect Power BI to Redshift and build reports from the dataset.  

---

## Author

**Gilbert Walker**  
Data Conversion Specialist transitioning into Data Engineering  
📍 Bethlehem, GA  
🔗 [GitHub Profile](https://github.com/GilbertWalker-DE)

---
