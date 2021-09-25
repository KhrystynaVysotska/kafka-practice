from producer.base_producer import BaseProducer
from secure.configs import PRODUCTS_SCHEMA_FILE_NAME, PRODUCTS_TOPIC_NAME


class ProductProducer(BaseProducer):
    def __init__(self):
        super().__init__(PRODUCTS_SCHEMA_FILE_NAME, PRODUCTS_TOPIC_NAME)