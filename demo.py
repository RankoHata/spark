from pyspark.sql import SparkSession

# 创建 SparkSession
spark = SparkSession.builder \
    .appName("SimpleSumTask") \
    .master("spark://spark-master:28814") \
    .getOrCreate()

# 创建一个包含 1 到 100 的整数的 RDD
numbers = spark.sparkContext.parallelize(range(1, 101))

# 计算整数之和
sum_result = numbers.sum()

print(f"The sum of numbers from 1 to 100 is: {sum_result}")

# 停止 SparkSession
spark.stop()
