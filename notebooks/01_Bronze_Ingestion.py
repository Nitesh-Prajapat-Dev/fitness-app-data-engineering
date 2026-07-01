# Databricks notebook source
from pyspark.sql.functions import *

users_df = spark.read.option("header",True).csv("/FileStore/users.csv",inferSchema=True)

steps_df = spark.read.option("header",True).csv("/FileStore/daily_steps.csv",inferSchema=True)

workout_df = spark.read.option("header",True).csv("/FileStore/workouts.csv",inferSchema=True)

heart_df = spark.read.option("header",True).csv("/FileStore/heart_rate.csv",inferSchema=True)

diet_df = spark.read.option("header",True).csv("/FileStore/diet_logs.csv",inferSchema=True)

sleep_df = spark.read.option("header",True).csv("/FileStore/sleep_logs.csv",inferSchema=True)

# COMMAND ----------

# DBTITLE 1,Cell 2
users_df = spark.read.option("header", True).csv(
    "abfss://fitness-data@fitnessstorage1.dfs.core.windows.net/landing/users/users.csv",
    inferSchema=True
)
users_df.write.mode("overwrite").format("delta").saveAsTable("bronze_users")

# COMMAND ----------

# DBTITLE 1,Cell 3
base = "abfss://fitness-data@fitnessstorage1.dfs.core.windows.net/landing"

steps_df = spark.read.option("header", True).csv(f"{base}/daily_steps/daily_steps.csv", inferSchema=True)
steps_df.write.mode("overwrite").format("delta").saveAsTable("bronze_daily_steps")

workout_df = spark.read.option("header", True).csv(f"{base}/workouts/workouts.csv", inferSchema=True)
workout_df.write.mode("overwrite").format("delta").saveAsTable("bronze_workouts")

heart_df = spark.read.option("header", True).csv(f"{base}/heart_rate/heart_rate.csv", inferSchema=True)
heart_df.write.mode("overwrite").format("delta").saveAsTable("bronze_heart_rate")

diet_df = spark.read.option("header", True).csv(f"{base}/diet_logs/diet_logs.csv", inferSchema=True)
diet_df.write.mode("overwrite").format("delta").saveAsTable("bronze_diet_logs")

sleep_df = spark.read.option("header", True).csv(f"{base}/sleep_logs/sleep_logs.csv", inferSchema=True)
sleep_df.write.mode("overwrite").format("delta").saveAsTable("bronze_sleep_logs")

# COMMAND ----------

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("abfss://fitness-data@fitnessstorage1.dfs.core.windows.net/landing/users/users.csv")

display(df)

# COMMAND ----------

# MAGIC %sql SHOW TABLES;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gold_user_health_summary LIMIT 10;

# COMMAND ----------

