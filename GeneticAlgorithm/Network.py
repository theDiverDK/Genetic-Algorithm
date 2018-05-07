import random


class Network:
    def __init__(self):
        self.population = 0
        self.agents = []

    def create(self, population, num, model):
        self.population = population
        self.model = model
        self.num = num

        for _ in range(self.population):
            input = 'HALLO'
            agent = self.model(len(input))
            agent.setInput(input)
            agent.initialize()

            self.agents.append(agent)

    def evaluate(self):
        for agent in self.agents:
            agent.evaluate()

    def selection(self):
        self.agents = sorted(
            self.agents, key=lambda agent: agent.fitness, reverse=True)

        self.agents = self.agents[:int(self.num * len(self.agents))]

    def crossover(self):
        print('model',self.model)
        offspring = []

        for _ in range(int(len(self.agents)/2) % 2):
            # Instead of pop, get random element
            parent1 = self.agents.pop()  # random.choice(self.agents)
            parent2 = self.agents.pop()  # random.choice(self.agents)

            child1 = self.model(parent1.length)
            child2 = self.model(parent1.length)

            split = random.randint(0, parent1.length-1)
            child1.data = parent1.data[0:split]+parent2.data[split:]
            child2.data = parent2.data[0:split]+parent1.data[split:]

            offspring.append(child1)
            offspring.append(child2)

        if(len(self.agents) > 0):
            offspring.append(self.agents.pop())

        self.agents = offspring

        for _ in range(self.population-len(self.agents)):
            agent = self.model(parent1.length)
            agent.setInput(parent1.inputString)
            agent.initialize()
            self.agents.append(agent)

    def __str__(self):
        return 'Population of {}\n'.format(self.population) + '\n'.join([x.__str__() for x in self.agents])
