# Electric Vehicle Data Engineering Project

## Overview
This project explores **Electric Vehicle (EV) adoption in the United States**. It is a **full data engineering pipeline** designed to extract, transform, and load EV data from multiple sources into analytics-ready databases.  

The goal of the project is to build an **end-to-end ETL workflow** that enables generating insights and visualizations about EV usage, trends, and patterns.  

---

## What the Project Does
- Extracts data from **public APIs**, **Google Cloud Storage (GCS)**, and **other BigQuery projects**.  
- Transforms raw data into **clean, structured, and analytics-ready datasets**.  
- Loads transformed data into **BigQuery** and **MySQL** for further analysis and reporting.  
- Automates the workflow using **Airflow DAGs** for daily scheduled runs.  
- Generates dashboards in **Looker Studio** for visualization and insights.  

---

## How the Project Was Done

### 1. Data Extraction
- Pulled EV data from **Data.gov datasets** and public APIs.  
- Ingested raw files from **GCS buckets**.  
- Queried data from **BigQuery tables in other projects** to consolidate information.  

### 2. Data Transformation
- Converted raw JSON and table data into **pandas DataFrames**.  
- Cleaned and normalized data: renamed columns, handled missing values, standardized formats.  
- Added derived metrics such as **total EV registrations per state** and **yearly growth trends**.  

### 3. Data Loading
- Loaded processed data into **BigQuery** for analytics and intermediate storage.  
- Loaded final transformed tables into **MySQL** for reporting dashboards.  
- Used **truncate & load** strategies to keep the data up-to-date and consistent.  

### 4. Pipeline Orchestration
- Built **Airflow DAGs** to automate the ETL process:
  - Extract from API → BigQuery  
  - Extract from GCS → BigQuery  
  - Extract from other BigQuery projects → BigQuery  
  - Transform and load → MySQL  
- Scheduled DAGs for **daily execution** and implemented **retry mechanisms** for reliability.  

### 5. Visualization
- Connected **Looker Studio** dashboards to BigQuery datasets.  
- Created visualizations to show:
  - EV adoption trends over time  
  - State-wise comparisons  
  - Growth in EV registrations  

### 6. Automation & CI/CD
- Used **Cloud Build triggers** to automatically deploy DAGs to **Cloud Composer** when code is pushed to GitHub.  
- Ensured the pipeline is **version-controlled** and **production-ready**.  

---

## Tech Stack
- **Python / Pandas** – Data extraction and transformation  
- **Google Cloud Platform (GCP)** – BigQuery, GCS, Cloud Composer  
- **Airflow** – ETL orchestration  
- **MySQL** – Final analytics-ready database  
- **Looker Studio** – Dashboards and visualization  
- **Cloud Build + GitHub** – CI/CD automation  

---

---

## Author
**Vinayak Shegar**  
Data Engineer | Pune, India  
[GitHub](https://github.com/iamVinayak50) | [LinkedIn](https://www.linkedin.com/in/vinayakshegar)








