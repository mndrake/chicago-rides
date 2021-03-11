# Databricks notebook source
# MAGIC %sql
# MAGIC use dave_carlson_databricks_com_chicago

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables

# COMMAND ----------

max_date = sql("select date_sub(max(trip_start_timestamp), 2) as max_date from chicago_taxi_trips").collect()[0]['max_date'].isoformat()

# COMMAND ----------

# MAGIC %sh
# MAGIC head -n 5 /tmp/taxi_trips_2018.csv

# COMMAND ----------

# MAGIC %sh
# MAGIC wget -O /tmp/taxi_delta.csv https://data.cityofchicago.org/resource/wrvz-psew.csv?%24where=trip_start_timestamp%20>=%20'2020-09-30T0:0:00.000'&%24limit=1000000000

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from taxi_trips

# COMMAND ----------

sql('use dave_carlson_databricks_com_db')
taxi = table('taxi_trips')

# COMMAND ----------

sql("use dave_carlson_databricks_com_chicago")

taxi.write \
  .format('delta') \
  .mode('overwrite') \
  .option('path', '/home/dave.carlson@databricks.com/datasets/chicago/taxi/delta') \
  .saveAsTable('chicago_taxi_trips')

# COMMAND ----------

sql('optimize chicago_taxi_trips')

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from taxi_trips

# COMMAND ----------


