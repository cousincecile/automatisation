import org.apache.spark.sql.{Encoders, SparkSession}
import org.apache.spark.sql.functions._
import Utilities.flattenStructSchema



object Main {
  def main(args: Array[String]): Unit = {

    val spark = SparkSession
      .builder()
      .appName("spotify_playlists_ingestion")
      .master("local[*]")
      .getOrCreate()

    val encoderSchema = Encoders.product[JsonObject].schema
    val df = spark.read.schema(encoderSchema).json("path_to_data")

    df.select(flattenStructSchema(df.schema):_*).withColumn("partition_date",lit(current_date()))
      .write.mode("overwrite").parquet("parquets_data/playlists/"+lit(current_date()))

  }
}
