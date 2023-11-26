from confluent_kafka import Producer
import subprocess
import json
import time
import argparse

# Function to get Docker container stats
def get_docker_stats(container_name):
    cmd = f"docker stats --no-stream {container_name}"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, text=True)
    return json.dumps(result.stdout.strip().split("\n")[1].split("   "))

# Function to send message to Kafka topic
def send_to_kafka(bootstrap_servers, kafka_topic, message):
    print(message)
    producer = Producer({'bootstrap.servers': bootstrap_servers})
    producer.produce(kafka_topic, key='docker_stats', value=message)
    producer.flush()

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Docker Stats to Kafka')
    parser.add_argument('container_name', type=str, help='Name of the Docker container')
    parser.add_argument('kafka_topic', type=str, help='Kafka topic to send messages to')
    args = parser.parse_args()

    # Set Kafka broker
    kafka_broker = 'localhost:9092'  # Update with your Kafka broker

    # Get Docker stats for a minute and send to Kafka topic
    for i in range(60):
        docker_stats = get_docker_stats(args.container_name)
        send_to_kafka(kafka_broker, args.kafka_topic, docker_stats)
        time.sleep(1)
