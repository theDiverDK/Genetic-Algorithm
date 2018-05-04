import random
import string

from fuzzywuzzy import fuzz
from GeneticAlgorithm.Models.BaseModel import BaseModel


class StringModel(BaseModel):
    def __init__(self, inputString):
        super(StringModel, self).__init__()

        self.length = len(inputString)
        self.data = None
        self.inputString = inputString

    def initialize(self):
        self.data = ''.join(random.SystemRandom().choice(
            string.ascii_uppercase) for _ in range(self.length))

    def evaluate(self):
        self.fitness = fuzz.ratio(self.data, self.inputString)

    def crossover(self):
        pass

    def mutate(self):
        pass

    def __str__(self):
        if self.data is None:
            return 'Not initialized'

        return self.data + ', fitness = ' + str(self.fitness)
