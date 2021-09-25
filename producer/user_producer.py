from producer.base_producer import BaseProducer
from secure.configs import USERS_SCHEMA_FILE_NAME, USERS_TOPIC_NAME


class UserProducer(BaseProducer):
    def __init__(self):
        super().__init__(USERS_SCHEMA_FILE_NAME, USERS_TOPIC_NAME)