from pyspark.sql import SparkSession
from pyspark.sql.functions import coalesce


def get_products_with_categories(products_df, categories_df):
    
    joined_df = products_df.join(categories_df, "product_id", "left")
 
    result_df = joined_df.select("product_name", coalesce("category_name", "Без категории").alias("category_name"))

    return result_df


spark = SparkSession.builder.getOrCreate()

products_df = spark.read.csv("products.csv", header=True)
categories_df = spark.read.csv("categories.csv", header=True)

result_df = get_products_with_categories(products_df, categories_df)

result_df.show()