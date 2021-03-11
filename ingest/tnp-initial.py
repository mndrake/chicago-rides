# Databricks notebook source
dbutils.fs.mkdirs('/home/dave.carlson@databricks.com/datasets/chicago/tnp/csv')

# COMMAND ----------

# MAGIC %sh
# MAGIC wget -O /tmp/tnp_trips_2018.csv https://data.cityofchicago.org/resource/rpfj-eb3a.csv?%24limit=1000000000

# COMMAND ----------

dbutils.fs.cp('file:/tmp/tnp_trips_2018.csv', 'dbfs:/home/dave.carlson@databricks.com/datasets/chicago/tnp/csv/tnp_trips_2018.csv')

# COMMAND ----------

# MAGIC %sh
# MAGIC wget -O /tmp/tnp_trips_2019.csv https://data.cityofchicago.org/resource/iu3g-qa69.csv?%24limit=1000000000

# COMMAND ----------

dbutils.fs.cp('file:/tmp/tnp_trips_2019.csv', 'dbfs:/home/dave.carlson@databricks.com/datasets/chicago/tnp/csv/tnp_trips_2019.csv')

# COMMAND ----------

# MAGIC %sh
# MAGIC wget -O /tmp/tnp_trips_2020.csv https://data.cityofchicago.org/resource/rmc8-eqv4.csv?%24limit=1000000000

# COMMAND ----------

dbutils.fs.cp('file:/tmp/tnp_trips_2020.csv', 'dbfs:/home/dave.carlson@databricks.com/datasets/chicago/tnp/csv/tnp_trips_2020.csv')

# COMMAND ----------

dbutils.fs.mkdirs('dbfs:/home/dave.carlson@databricks.com/datasets/chicago/taxi/csv/')

# COMMAND ----------

# MAGIC %sh
# MAGIC wget -O /tmp/taxi_trips_2018.csv https://data.cityofchicago.org/resource/vbsw-zws8.csv?%24limit=1000000000

# COMMAND ----------

dbutils.fs.cp('file:/tmp/taxi_trips_2018.csv', 'dbfs:/home/dave.carlson@databricks.com/datasets/chicago/taxi/csv/taxi_trips_2018.csv')

# COMMAND ----------

# MAGIC %sh
# MAGIC wget -O /tmp/taxi_trips_2019.csv https://data.cityofchicago.org/resource/h5cq-z3dy.csv?%24limit=1000000000

# COMMAND ----------

dbutils.fs.cp('file:/tmp/taxi_trips_2019.csv', 'dbfs:/home/dave.carlson@databricks.com/datasets/chicago/taxi/csv/taxi_trips_2019.csv')

# COMMAND ----------

#%sh
#wget -O /tmp/taxi_trips_2020.csv https://data.cityofchicago.org/resource/h5cq-z3dy.csv?%24limit=1000000000

# COMMAND ----------

#dbutils.fs.cp('file:/tmp/taxi_trips_2020.csv', 'dbfs:/home/dave.carlson@databricks.com/datasets/chicago/taxi/csv/taxi_trips_2020.csv')
