# Databricks notebook source
users = spark.table("silver_users")
steps = spark.table("silver_daily_steps")
diet = spark.table("silver_diet_logs")
sleep = spark.table("silver_sleep_logs")

# COMMAND ----------

from pyspark.sql.functions import avg

avg_steps = steps.groupBy("user_id").agg(avg("steps").alias("avg_steps"))

avg_sleep = sleep.groupBy("user_id").agg(avg("sleep_hours").alias("avg_sleep"))

avg_calories = diet.groupBy("user_id").agg(avg("calories_intake").alias("avg_calories"))

# COMMAND ----------

gold = users.join(avg_steps, "user_id", "left") \
            .join(avg_sleep, "user_id", "left") \
            .join(avg_calories, "user_id", "left")

# COMMAND ----------

gold.write.mode("overwrite").saveAsTable("gold_user_health_summary")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM gold_user_health_summary LIMIT 10;

# COMMAND ----------

# MAGIC %sql DESCRIBE gold_user_health_summary

# COMMAND ----------

