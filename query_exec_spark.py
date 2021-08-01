from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import col
import sys

sc = SparkContext('local')
spark = SparkSession(sc)
log4jLogger = sc._jvm.org.apache.log4j 
log = log4jLogger.LogManager.getLogger(__name__)

try:
	df_read_vendors = spark.read.options(header='True', inferSchema='True', delimiter=',').csv(sys.argv[1])
	df_read_orders = spark.read.options(header='True', inferSchema='True', delimiter=',').csv(sys.argv[2])
	df_read_vendors_rm=df_read_vendors.withColumnRenamed("id","vid")
	df_join_ov = df_read_orders.join(df_read_vendors_rm,df_read_orders.vendor_id ==  df_read_vendors_rm.vid,"left")
	df_final_data=df_join_ov.filter( (df_join_ov.status==2) | (df_join_ov.status==3)).groupBy("vid").sum("amt").orderBy(col("sum(amt)").desc()).limit(3)
	df_final_data.show()
	log.info("Job Ended Successfully")
except Exception as e:
	print("Job failed because of the following reason - ", e)
	log.info("Job Failed")