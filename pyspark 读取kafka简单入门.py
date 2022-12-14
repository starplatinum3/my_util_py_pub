#encoding=utf8
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import kafka
import json
offsets = []
def out_put(m):
    print(m)
def store_offset(rdd):
    global offsets
    offsets = rdd.offsetRanges()
    return rdd
 
def print_offset(rdd):
    for o in offsets:
        print "%s %s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset,o.untilOffset-o.fromOffset)
 
 
#  https://blog.csdn.net/u013496080/article/details/82085636
config = SparkConf()
scontext = SparkContext(appName='kafka_pyspark_test',)
stream_context = StreamingContext(scontext,2)
msg_stream = KafkaUtils.createDirectStream(stream_context,['asin_bsr_result',],kafkaParams={"metadata.broker.list": "3.120.9.44:9092,"})
result = msg_stream.map(lambda x :json.loads(x).keys()).reduce(out_put)
msg_stream.transform(store_offset,).foreachRDD(print_offset)
result.pprint()
stream_context.start()
stream_context.awaitTermination()
 
 