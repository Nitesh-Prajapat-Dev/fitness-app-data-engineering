# Fitness Data Engineering Project

## Project Overview

This project demonstrates an end-to-end Azure Data Engineering pipeline for fitness data analytics using the Medallion Architecture (Bronze, Silver and Gold).

## Tech Stack

- Azure Data Lake Storage Gen2
- Azure Databricks
- Azure Data Factory
- PySpark
- Delta Lake
- Power BI
- GitHub

## Architecture

CSV Files
↓
ADLS Landing
↓
ADF Pipeline
↓
Bronze Layer
↓
Silver Layer
↓
Gold Layer
↓
Power BI Dashboard

## Dataset

The project contains:

- Users
- Daily Steps
- Workouts
- Heart Rate
- Diet Logs
- Sleep Logs

## Bronze Layer

- Reads raw CSV files from ADLS
- Stores raw data into Delta tables

## Silver Layer

- Removes duplicate records
- Handles null values
- Filters invalid records
- Performs data validation

## Gold Layer

Business KPIs:

- Average Daily Steps
- Average Sleep Hours
- Average Calories Intake
- Total Workout Duration
- Average Heart Rate

## Dashboard

Power BI dashboard includes:

- Total Users
- Average Steps
- Average Sleep
- Average Calories
- Gender Distribution
- User Health Summary

## Project Structure

```
Fitness-App-Data-Engineering
│
├── datasets
├── notebooks
├── scripts
├── README.md
├── requirements.txt
└── .gitignore
```