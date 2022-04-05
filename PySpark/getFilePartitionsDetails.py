from pyspark.sql import SparkSession, functions as f
from pyspark.sql.functions import spark_partition_id

spark = SparkSession.builder\
    .appName("pySparkSCD1App")\
    .getOrCreate()
    
path = "/user/itv000197/customer.csv"

df_source_data = spark.read \
        .format("csv") \
        .option("path", path) \
        .option("header", True) \
        .load()
df_target_data = spark.read \
        .format("parquet") \
        .option("path", "/user/itv000197/output/") \
        .option("header", True) \
        .load()
        
df_source_data.select(f.input_file_name().alias("FILE_NAME")).distinct().show(truncate=False)

df_target_data.select(f.input_file_name().alias("FILE_NAME")).distinct().show(truncate=False)


# get the counts of records in each partiton 
df_big_data.withColumn("partitionId", spark_partition_id()).groupBy("partitionId").count().orderBy("partitionId").show()

# get the counts of records in each partiton using mapPartitionsWithIndex
def count_in_a_partition(idx, iterator):
  count = 0
  for _ in iterator:
    count += 1
  yield (idx,count)

df_big_data.rdd.mapPartitionsWithIndex(count_in_a_partition).collect()
