from abc import ABC, abstractmethod


class BaseModel(ABC):
    def __init__(self):
        self.fitness = -1

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def mutate(self):
        pass
