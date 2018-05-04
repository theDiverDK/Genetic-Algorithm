import random
import string
from GeneticAlgorithm.BaseModel import BaseModel


class StringModel(BaseModel):
    def __init__(self):
        super(StringModel, self).__init__()

        self.length = 20
        self.data = None

    def initialize(self):
        self.data = ''.join(random.SystemRandom().choice(
            string.ascii_uppercase) for _ in range(self.length))

    def __str__(self):
        if self.data is None:
            return 'Not initialized'

        return self.data
