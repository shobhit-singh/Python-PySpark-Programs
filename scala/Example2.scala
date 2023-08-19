package com

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{col, lit, regexp_extract, udf}

object parseLogsCustom extends App {

  val spark: SparkSession = SparkSession
    .builder()
    .master("local[1]")
    .appName("learn")
    .getOrCreate()

  spark.sparkContext.setLogLevel("ERROR")
  import spark.implicits._

  val regex =
    """^(\S+)\s+(\S+)\s+\[([^\]]+)\]\s+"([A-Z]+)\s+(\S+)\s+HTTP/([0-9.]+)"\s+([0-9]{3})\s+([0-9]+)\s+"([^"]+)"\s+"([^"]+)"\s+"([^"]+)"$"""
  
  val col_pos_map = Map(
    (0, "host"),
    (1, "userid"),
    (2, "datetime"),
    (3, "method"),
    (4, "request"),
    (5, "http_version"),
    (6, "status"),
    (7, "size"),
    (8, "other_data"),
    (9, "referer"),
    (10, "user_agent")
  )

  val df = spark.read.textFile("logs_data.txt")

  val udf_regex_split = udf((input_column: String, regex: String) => {
    regex.r.unapplySeq(input_column)
  })

  val df_parsed =
    df.withColumn("parsed_fields", udf_regex_split($"value", lit(regex)))

  val finalDF = df_parsed.select(
    col_pos_map.keys.toList.map(x =>
      col("parsed_fields")(x).as(col_pos_map(x))
    ): _*
  )

  finalDF
    .select(
      "host",
      "userid",
      "datetime",
      "method",
      "http_version",
      "status",
      "size"
    )
    .show(false)
}
