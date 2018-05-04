
class Network:
    def __init__(self):
        self.population = 0
        self.agents = []

    def create(self, population, num, model):
        self.population = population
        self.model = model
        self.num = num

        for _ in range(self.population):
            agent = self.model('HALLO')
            agent.initialize()

            self.agents.append(agent)

    def evaluate(self):
        for agent in self.agents:
            agent.evaluate()

    def selection(self):
        self.agents = sorted(self.agents, key=lambda agent: agent.fitness, reverse=True)
        self.agents = self.agents[:int(self.num * len(self.agents))]

    def __str__(self):
        return 'Population of {}'.format(self.population)
