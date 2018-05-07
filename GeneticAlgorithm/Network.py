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
        offspring = []

        #for _ in range(int((self.population - len(self.agents)) / 2)):
        parent1 = random.choice(self.agents)
        parent2 = random.choice(self.agents)
        child1 = self.model(parent1.length).initialize()
        child2 = self.model(parent2.length).initialize()
        split = random.randint(0,parent1.length)

        d1 = parent1.data[0:split] + parent2.data[split:parent1.length]
        d2 = parent2.data[0:split] + parent1.data[split:parent2.length]

        print(child1)
        child1.data=d1

        print(child1)
        offspring.append(child1)
        offspring.append(child2)

        # self.agents.extend(offspring)

    def __str__(self):
        return 'Population of {}\n'.format(self.population) + '\n'.join([x.__str__() for x in self.agents])
