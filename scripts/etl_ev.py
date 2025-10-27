from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

spark = SparkSession.builder.appName("EV_ETL").getOrCreate()

# -------- EXTRACT --------
df = spark.read.csv(
    "gs://ev-market-data/raw/ev_sales_by_makers_and_cat_15-24.csv",
    header=True,
    inferSchema=True
)

# -------- TRANSFORM --------
df_clean = (
    df.select("Maker", "Vehicle_Class", "Year", "Month", "Sales")
      .dropna(subset=["Maker", "Vehicle_Class", "Year", "Sales"])
      .filter(col("Year") >= 2020)
)

df_agg = (
    df_clean.groupBy("Maker", "Year")
            .agg(_sum("Sales").alias("Total_Sales"))
            .orderBy("Year", ascending=False)
)

# -------- LOAD --------
df_agg.write.format("bigquery") \
    .option("table", "boxwood-axon-470816-b1.ev_dataset.ev_sales_cleaned") \
    .option("temporaryGcsBucket", "ev-pipeline-temp") \
    .mode("overwrite") \
    .save()

spark.stop()
print("✅ ETL job completed!")
