import json
from secure.configs import *
from confluent_kafka.avro import AvroProducer
from utils.schema_uploader import SchemaUploader


class BaseProducer:
    def __init__(self, schema_file_name, topic_name):
        self.topic_name = topic_name

        self.producer_config = {
            "bootstrap.servers": BOOTSTRAP_SERVERS_URL,
            "schema.registry.url": SCHEMA_REGISTRY_URL
        }

        key_schema, value_schema = SchemaUploader.load_avro_schema_from_file(schema_file_name)

        self.producer = AvroProducer(
            self.producer_config,
            default_key_schema=key_schema,
            default_value_schema=value_schema
        )

    def send_record(self, key: str, value: json):
        try:
            self.producer.produce(topic=self.topic_name, key=key, value=value)
        except Exception as e:
            print(f"Exception while producing record value - {value} to topic - {self.topic_name}: {e}")
        else:
            print(f"Successfully producing record value - {value} to topic - {self.topic_name}")

    def send_records(self, messages: list):
        for message in messages:
            self.send_record(key=message.key, value=message.to_json())
        self.producer.flush()