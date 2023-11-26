package eventProcessor;

import models.SkyOneAirlinesFlightData;
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.Offsets Initializer;
import org.apache.flink. formats.json.JsonDeserializationSchema;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment. StreamExecutionEnvironment;
import java.io.InputStream;
import java.util. Properties;