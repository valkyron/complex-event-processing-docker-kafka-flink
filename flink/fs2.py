from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, CsvTableSource, DataTypes
from pyflink.table.descriptors import Schema, Kafka, Json

def consume_kafka_messages():
    # Create a StreamExecutionEnvironment.
    env = StreamExecutionEnvironment.get_execution_environment()

    # Create a StreamTableEnvironment.
    table_env = StreamTableEnvironment.create(env)

    # Register Kafka Topic 1 as a table.
    table_env.connect(Kafka()
                        .version("universal")
                        .topic("docker_stats")
                        .start_from_latest()
                        .property("zookeeper.connect", "localhost:2181")
                        .property("bootstrap.servers", "localhost:9092")).with_format(Json().derive_schema()).with_schema(Schema().schema(DataTypes.ROW([DataTypes.FIELD("field1", DataTypes.STRING()),
                                                DataTypes.FIELD("field2", DataTypes.INT())]))).in_append_mode().register_table_source("docker_stats")

    # Register Kafka Topic 2 as a table.
    table_env.connect(Kafka()
                        .version("universal")
                        .topic("docker_stats2")
                        .start_from_latest()
                        .property("zookeeper.connect", "localhost:2181")
                        .property("bootstrap.servers", "localhost:9092")).with_format(Json().derive_schema()).with_schema(Schema().schema(DataTypes.ROW([DataTypes.FIELD("field1", DataTypes.STRING()),
                                                DataTypes.FIELD("field2", DataTypes.INT())]))).in_append_mode().register_table_source("docker_stats2")

    # Perform a join between the two tables.
    table_result = table_env.sql_query("""
        SELECT t1.field1, t1.field2, t2.field1, t2.field2
        FROM kafka_topic_1 AS t1
        JOIN kafka_topic_2 AS t2
        ON t1.field1 = t2.field1
    """)

    # Print the results to the standard output.
    table_result.print()

    # Execute the job.
    env.execute("consume_kafka_messages")

if __name__ == "__main__":
    consume_kafka_messages()