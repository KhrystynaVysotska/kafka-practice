import random
from faker import Faker
from entities.entity import Entity


class Product(Entity):
    def __init__(self, barcode: str, category: str, name: str, price: int, description: str):
        self.key = barcode
        self.barcode = barcode
        self.category = category
        self.name = name
        self.price = price
        self.description = description

    @staticmethod
    def generate_random_entity():
        faker = Faker()
        fake_name = faker.word()
        fake_price = faker.pricetag()
        fake_barcode = faker.ean(length=13)
        fake_description = faker.text(max_nb_chars=50)
        fake_category = random.choice(['Food', 'Vehicle', 'Clothes', 'Household appliances', 'Drinks', 'Toys'])

        return Product(
            barcode=fake_barcode,
            category=fake_category,
            name=fake_name,
            price=fake_price,
            description=fake_description
        )
