from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer

env = StreamExecutionEnvironment.get_execution_environment()

# Set up Kafka consumer for topic1
properties1 = {'bootstrap.servers': 'localhost:9092', 'group.id': 'group1'}
source1 = FlinkKafkaConsumer('docker_stats', SimpleStringSchema(), properties1)
source1.set_jar_files(['./flink-sql-connector-kafka_2.11-1.13.0.jar'])

# Set up Kafka consumer for topic2
properties2 = {'bootstrap.servers': 'localhost:9092', 'group.id': 'group2'}
source2 = FlinkKafkaConsumer('docker_stats2', SimpleStringSchema(), properties2)
source2.set_jar_files(['./flink-sql-connector-kafka_2.11-1.13.0.jar'])

# Add sources to the environment
stream1 = env.add_source(source1)
stream2 = env.add_source(source2)

# Process data (you can define your processing logic here)

# Print the results to stdout for testing
stream1.print()
stream2.print()

# Execute the job
env.execute("Flink Kafka Job")
