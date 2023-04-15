import sys
sys.path.append('./utils')
from spark_config import spark_configs

spark = spark_configs()

spark = spark.builder.appName('read spark').getOrCreate()

#Extract
# cnaes = spark.read.format('csv').option('header','true').option('delimiter',';').load('../data/cnaes.csv')
# estabelecimentos = spark.read.format('csv').option('header','true').option('delimiter',';').load('../data/estabelecimentos/')


#Load
# cnaes.write.format('parquet').mode('overwrite').save('../data/ceaes')
# estabelecimentos.write.format('parquet').mode('overwrite').save('../data/estabelecimentos2')