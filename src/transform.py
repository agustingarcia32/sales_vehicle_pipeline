from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, regexp_replace
from pyspark.sql import functions as F
import os
import shutil


spark= SparkSession.builder.appName("transform_data").getOrCreate()

df= spark.read.csv("data/raw/cars_raw.csv", header=True, inferSchema=True)
df.show()
df.printSchema()

# Eliminar columnas no deseadas
df = df.drop('color', 'interior', 'saledate', 'odometer', 'vin', 'mmr', 'condition')


# Verificar si hay valores nulos
df.select([sum(col(c).isNull().cast("int")).alias(c) for c in df.columns]).show()

# Eliminar filas con valores nulos en 'rating_count'
df = df.dropna(subset=["make", "model", "trim", "body", "transmission", "sellingprice"])
df.count()


df = df.dropDuplicates()
df.count()

df = df.withColumnRenamed('make', 'brand')
df.show()


# Agrupar por marca y calcular el conteo y la suma de 'sellingprice' para cada marca
df_grouped = df.groupBy("brand").agg(
    F.count("brand").alias("count"), 
    F.sum("sellingprice").alias("total_price")
)

# Mostrar el resultado
df_grouped.show()

# Guardar en un solo archivo CSV
output_folder = "data/processed/sales_processed"
df_grouped.coalesce(1).write.csv(output_folder, header=True, mode="overwrite")

# Renombrar el archivo generado
final_filename = "sales_processed.csv"

# Buscar el archivo dentro de la carpeta y renombrarlo
for file in os.listdir(output_folder):
    if file.startswith("part-") and file.endswith(".csv"):
        shutil.move(os.path.join(output_folder, file), os.path.join("data/processed", final_filename))
        break

# Eliminar la carpeta vacía que creó PySpark
shutil.rmtree(output_folder)

# Finalizar Spark
spark.stop()
