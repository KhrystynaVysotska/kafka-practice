from abc import ABC, abstractmethod


class Entity(ABC):

    def to_json(self) -> dict:
        return self.__dict__

    @staticmethod
    @abstractmethod
    def generate_random_entity():
        raise NotImplementedError
