import random
import string

from fuzzywuzzy import fuzz
from GeneticAlgorithm.Models.BaseModel import BaseModel


class StringModel(BaseModel):
    def __init__(self, length):
        super(StringModel, self).__init__()

        self.length = length
        self.data = None
        self.inputString = ''

    def setInput(self, inputString):
        self.inputString = inputString

    def initialize(self):
        self.data = ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(self.length))

    def evaluate(self):
        self.fitness = fuzz.ratio(self.data, self.inputString)

    def mutate(self):
        for idx, param in enumerate(self.data):
            if random.uniform(0.0, 1.0) <= 0.1:
                self.data = self.data[0:idx] + random.choice(string.ascii_letters) + self.data[idx + 1:]

    def crossover(self):
        pass

    def __str__(self):
        if self.data is None:
            return 'Not initialized'

        return self.data + ', fitness = ' + str(self.fitness)
