package com
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.regexp_extract

object parseLogs extends App {

  val spark: SparkSession = SparkSession
    .builder()
    .master("local[1]")
    .appName("learn")
    .getOrCreate()
    
  spark.sparkContext.setLogLevel("ERROR")
  import spark.implicits._

  val regex =
    """^(\S+)\s+(\S+)\s+\[([^\]]+)\]\s+"([A-Z]+)\s+(\S+)\s+HTTP/([0-9.]+)"\s+([0-9]{3})\s+([0-9]+)\s+"([^"]+)"\s+"([^"]+)"\s+"([^"]+)"$"""

  val df = spark.read.textFile("logs_data.txt")

  val final_df = df.select(
    regexp_extract($"value", regex, 1).as("host"),
    regexp_extract($"value", regex, 2).as("userid"),
    regexp_extract($"value", regex, 3).as("datetime"),
    regexp_extract($"value", regex, 4).as("method"),
    regexp_extract($"value", regex, 5).as("request"),
    regexp_extract($"value", regex, 6).as("http_version"),
    regexp_extract($"value", regex, 7).as("status"),
    regexp_extract($"value", regex, 8).as("size"),
    regexp_extract($"value", regex, 9).as("other_data"),
    regexp_extract($"value", regex, 10).as("referer"),
    regexp_extract($"value", regex, 11).as("user_agent")
  )

  final_df.printSchema()

  final_df
    .select(
      "host",
      "userid",
      "datetime",
      "method",
      "http_version",
      "status",
      "size"
    )
    .show(5,false)

}
