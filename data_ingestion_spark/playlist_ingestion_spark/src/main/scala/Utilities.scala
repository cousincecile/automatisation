import org.apache.spark.sql.Column
import org.apache.spark.sql.functions.col
import org.apache.spark.sql.types.StructType

object Utilities {
  def flattenStructSchema(schema: StructType, prefix: String = null): Array[Column] = {
    schema.fields.flatMap(f => {
      val columnName = if (prefix == null) f.name else (prefix + "." + f.name)

      f.dataType match {
        case st: StructType => flattenStructSchema(st, columnName)
        case _ => if (!columnName.contains(".")) {
          Array(col(columnName).as(("music." + columnName).replace(".", "_")))
        }
        else {
          Array(col(columnName).as(columnName.replace(".", "_")))
        }
      }
    })
  }
}