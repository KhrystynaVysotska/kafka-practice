from producer.user_producer import UserProducer
from generator.user_generator import UserGenerator


def produce_users():
    user_producer = UserProducer()
    for users in UserGenerator.generate():
        user_producer.send_records(users)


if __name__ == '__main__':
    produce_users()
