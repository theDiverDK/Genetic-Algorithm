
class Network:
    def __init__(self):
        self.population = 0
        self.agents = []

    def create(self, population, model):
        self.population = population
        self.model = model

        for _ in range(self.population):
            agent = self.model()
            agent.initialize()

            self.agents.append(agent)

    def __str__(self):
        return 'Population of {}'.format(self.population)
