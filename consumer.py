



from kafka import KafkaConsumer
consumer = KafkaConsumer('RDD1.ipynb')
for msg in consumer:
    print (msg)

