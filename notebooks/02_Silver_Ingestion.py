# Databricks notebook source
from pyspark.sql.functions import *

users = spark.table("bronze_users")
steps = spark.table("bronze_daily_steps")
workout = spark.table("bronze_workouts")
heart = spark.table("bronze_heart_rate")
diet = spark.table("bronze_diet_logs")
sleep = spark.table("bronze_sleep_logs")

# COMMAND ----------

users = users.dropDuplicates()

steps = steps.filter(col("steps") > 0)

workout = workout.filter(col("duration_minutes") > 0)

heart = heart.filter((col("avg_heart_rate") > 30) & (col("avg_heart_rate") < 220))

diet = diet.na.fill({"calories_intake": 0})

sleep = sleep.dropDuplicates()

# COMMAND ----------

users.write.mode("overwrite").saveAsTable("silver_users")
steps.write.mode("overwrite").saveAsTable("silver_daily_steps")
workout.write.mode("overwrite").saveAsTable("silver_workouts")
heart.write.mode("overwrite").saveAsTable("silver_heart_rate")
diet.write.mode("overwrite").saveAsTable("silver_diet_logs")
sleep.write.mode("overwrite").saveAsTable("silver_sleep_logs")