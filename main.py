from entities.user import User
from entities.product import Product
from producer.user_producer import UserProducer
from producer.product_producer import ProductProducer
from generator.entity_generator import EntityGenerator


def produce_users():
    user_producer = UserProducer()
    for users in EntityGenerator.generate(User):
        user_producer.send_records(users)


def produce_products():
    product_producer = ProductProducer()
    for products in EntityGenerator.generate(Product):
        product_producer.send_records(products)


if __name__ == '__main__':
    produce_users()
    produce_products()
