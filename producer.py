#from kafka import KafkaProducer
#creating a producer for the kafka
#producer = KafkaProducer(bootstrap_servers=['192.168.0.10:9092'])

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:2181')
for _ in range(10):
    producer.send('foobar', b'some_message_bytes')