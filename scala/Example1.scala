package org.example
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{array, col, collect_set, explode, struct}

object Example1 {

  def main(args: Array[String]): Unit = {

    val spark:SparkSession = SparkSession.builder().master("local[1]")
      .appName("learn")
      .getOrCreate()

    val inputdf = spark.read.option("multiline","false").json("C:\\Users\\Shobh\\OneDrive\\Desktop\\source_file.json")

    val newdf1 = inputdf.withColumn("cust_detail_exploded",explode(col("cust_detail"))).drop("cust_detail")

    val newdf2 = newdf1.select( "cust_id", "emp_name","emp_id","cust_detail_exploded.mobile", "cust_detail_exploded.acc_no","cust_detail_exploded.name")

    val newdf3 = newdf2.groupBy("cust_id").agg(array(struct(collect_set(col("mobile")).as("mobile"),collect_set(col("acc_no")).as("acc_no"),collect_set(col("name")).as("name"))).as("cust_detail") )

    newdf3.printSchema()

    newdf3.write.json("C:\\Users\\Shobh\\OneDrive\\Desktop\\newww.txt")

  }
}
