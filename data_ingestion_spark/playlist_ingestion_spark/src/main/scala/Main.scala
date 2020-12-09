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
    val df_to_parquet = spark.read.schema(encoderSchema).json("path_to_data")

    df_to_parquet.select(flattenStructSchema(df_to_parquet.schema):_*)
      .withColumn("partition_date",lit(current_date())).
      write.mode("overwrite").parquet("parquets_data/playlists/"+lit(current_date()))

    val df_to_hive = spark.read.parquet("parquets_data/albums/"+lit(current_date()))

    df_to_hive.write.mode("append")
      .partitionBy("partition_date").saveAsTable("iabd1_groupe5.spotify_playlists")

  }
}
