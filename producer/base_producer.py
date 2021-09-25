import json
from abc import abstractmethod, ABC
from confluent_kafka.avro import AvroProducer
from utils.schema_uploader import SchemaUploader


class BaseProducer(ABC):
    def __init__(self, args):
        self.producer_config = {
            "bootstrap.servers": args.bootstrap_servers,
            "schema.registry.url": args.schema_registry
        }

        self.topic = args.topic

        key_schema, value_schema = SchemaUploader.load_avro_schema_from_file(args.schema_file)

        self.producer = AvroProducer(
            self.producer_config,
            default_key_schema=key_schema,
            default_value_schema=value_schema
        )

    @abstractmethod
    def send_record(self, key: str, value: json):
        raise NotImplementedError
