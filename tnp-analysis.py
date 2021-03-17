# Databricks notebook source
sql("use dave_carlson_databricks_com_chicago")

# COMMAND ----------

tnp_schema = """
  trip_id string,
  trip_start_timestamp timestamp,
  trip_end_timestamp timestamp,
  trip_seconds numeric,
  trip_miles numeric,
  pickup_census_tract string,
  dropoff_census_tract string,
  pickup_community_area int,
  dropoff_community_area int,
  fare numeric,
  tip numeric,
  additional_charges numeric,
  trip_total numeric,
  shared_trip_authorized boolean,
  trips_pooled int,
  pickup_centroid_latitude numeric,
  pickup_centroid_longitude numeric,
  pickup_centroid_location string,
  dropoff_centroid_latitude numeric,
  dropoff_centroid_longitude numeric,
  dropoff_centroid_location string
"""

tnp = spark.read.csv('/home/dave.carlson@databricks.com/datasets/chicago/tnp/csv', header=True, schema=tnp_schema)

# COMMAND ----------

display(tnp)

# COMMAND ----------

tnp.write \
  .format('delta') \
  .mode('overwrite') \
  .option('path', '/home/dave.carlson@databricks.com/datasets/chicago/tnp/delta') \
  .saveAsTable('chicago_tnp_trips')

# COMMAND ----------

sql('optimize chicago_tnp_trips')

# COMMAND ----------

# MAGIC %sql
# MAGIC with cte as (
# MAGIC   select
# MAGIC     date_format(trip_start_timestamp, 'yyyy-MM-dd') as trip_day,
# MAGIC     *
# MAGIC from chicago_tnp_trips
# MAGIC )
# MAGIC 
# MAGIC select 
# MAGIC   trip_day,
# MAGIC   count(*) as cnt
# MAGIC from cte
# MAGIC group by
# MAGIC   trip_day
# MAGIC order by
# MAGIC   1 asc

# COMMAND ----------

# MAGIC %md
# MAGIC new comment
