from confluent_kafka import Consumer, KafkaError

# Define Kafka broker and topic
kafka_broker = 'localhost:9092'
kafka_topic = 'docker_stats'

# Consumer configuration
consumer_conf = {
    'bootstrap.servers': kafka_broker,
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Create Kafka consumer
consumer = Consumer(consumer_conf)

# Subscribe to the topic
consumer.subscribe([kafka_topic])

try:
    while True:
        # Poll for messages
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                continue
            else:
                print(msg.error())
                break

        # Print the received message
        print('Received message: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    # Close down consumer to commit final offsets.
    consumer.close()
