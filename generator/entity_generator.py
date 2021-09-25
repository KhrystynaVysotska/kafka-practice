from time import sleep
from typing import List
from random import Random


class EntityGenerator:

    @staticmethod
    def generate(entity, amount_of_batches: int = 10, batch_size_from: int = 50, batch_size_to: int = 100) -> List:
        for i in range(amount_of_batches):
            entities = []
            batch_size = Random().randint(a=batch_size_from, b=batch_size_to)
            print(f"Batch #{i + 1} size {batch_size}")
            for _ in range(batch_size):
                entities.append(entity.generate_random_entity())
            yield entities
            sleep(5)
