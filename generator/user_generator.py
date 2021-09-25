from random import Random
from time import sleep
from typing import List

from entities.user import User


class UserGenerator(object):

    @staticmethod
    def generate(amount_of_batches: int = 10, batch_size_from: int = 50, batch_size_to: int = 100) -> List:
        for i in range(amount_of_batches):
            users: List[User] = list()
            batch_size = Random().randint(a=batch_size_from, b=batch_size_to)
            print(f"Batch #{1} size {batch_size}")
            for _ in range(batch_size):
                users.append(User.generate_random_user())
            yield users
            sleep(5)
