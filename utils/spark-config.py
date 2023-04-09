#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
from pyspark import SparkContext

def spark_configs():

    #Setting spark configs
    spark_jars = '''
        '''
    
    conf = (
            SparkConf()
            .set('spark.sql.repl.eagerEval.enabled', True)
            .set('spark.sql.execution.arrow.pyspark.enabled', True)
            .set('spark.sql.session.timeZone', 'UTC')
            .set('spark.sql.parquet.int96RebaseModeInRead', 'LEGACY')
            .set('spark.sql.parquet.int96RebaseModeInWrite', 'LEGACY')
            .set('spark.sql.parquet.datetimeRebaseModeInRead', 'LEGACY')
            .set('spark.sql.parquet.datetimeRebaseModeInWrite', 'LEGACY')
            .set('spark.network.timeout', '100000000')
            .set('spark.executor.heartbeatInterval', '100000000')
            .set('spark.executor.memory', '4G') #quanto aloca memória local
            .set('spark.driver.memory', '4G') #quanto de dados pode trafegar
            .set('spark.memory.offHeap.enabled', 'true')
            .set('spark.memory.offHeap.size', '4G' )
            .set('spark.sql.autoBroadcastJoinThreshold', '-1')
            .set('spark.sql.broadcastTimeout', '300000')  
            .set('spark.executor.cores', '8') #quantos cores
            .set('spark.executor.instances', '8')
            .set('spark.default.parallelism', '2') #especifica para rodar 2 fluxos em paralelo
            .set('spark.sql.debug.maxToStringFields', 1000)
            .set('spark.serializer', 'org.apache.spark.serializer.KryoSerializer') #organizar em série
            .set('spark.jars', spark_jars)
            .set('spark.ui.showConsoleProgress', True)
            .set('spark.logConf', True)
            .set('spark.driver.bindAddress', '0.0.0.0')
            .set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            .set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        )

    spark = (
            SparkSession
            .builder
            .config(conf=conf)
            .config("spark.jars.packages", "io.delta:delta-core_2.12:2.0.2")
            .master('local[*]')
            .appName('PySpark')
            .getOrCreate()
        )        
    

    spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
    spark._jsc.hadoopConfiguration().set("com.amazonaws.services.s3.enableV4", "true")
    spark._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider","org.apache.hadoop.fs.s3a.BasicAWSCredentialsProvider")
    spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "us-east-1.amazonaws.com")
    spark._jsc.hadoopConfiguration().set("fs.s3.fast.upload", "true") 
    spark._jsc.hadoopConfiguration().set("fs.s3.buffer.dir", "/tmp")


    return spark
