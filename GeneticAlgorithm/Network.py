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
            input = 'SorenReinke'
            agent = self.model(len(input))
            agent.setInput(input)
            agent.initialize()

            self.agents.append(agent)

    def evaluate(self):
        for agent in self.agents:
            agent.evaluate()

    def selection(self):
        self.agents = sorted(self.agents, key=lambda agent: agent.fitness, reverse=True)

        self.agents = self.agents[:int(self.num * len(self.agents))]

    def crossover(self):
        siblings = []

        for _ in range(int((self.population - len(self.agents)) / 2)):
            parent1 = random.choice(self.agents)
            parent2 = random.choice(self.agents)

            splitPoint = random.randint(0, parent1.length - 1)

            child1 = self.model(parent1.length)
            child1.setInput(parent1.inputString)
            child1.initialize()

            child2 = self.model(parent1.length)
            child2.setInput(parent1.inputString)
            child2.initialize()

            child1.data = parent1.data[0:splitPoint] + parent2.data[splitPoint:]
            child2.data = parent2.data[0:splitPoint] + parent1.data[splitPoint:]

            siblings.append(child1)
            siblings.append(child2)

        self.agents.extend(siblings)
        # availableNodes = [x for x in range(0, len(self.agents))]
        # while len(availableNodes) >= 2:
        #     random.shuffle(availableNodes)

        #     node1 = self.agents[availableNodes.pop()]
        #     node2 = self.agents[availableNodes.pop()]

        #     data1 = node1.data
        #     data2 = node2.data

        #     split = random.randint(0, len(data1) - 1)

        #     node1.data = data1[0:split] + data2[split:]
        #     node2.data = data1[0:split] + data2[split:]

        # for _ in range(self.population - len(self.agents)):
        #     temp=self.agents[0]
        #     agent=self.model(len(temp.data))
        #     agent.setInput(temp.inputString)
        #     agent.initialize()

        #     self.agents.append(agent)

    def mutate(self):
        for agent in self.agents:
            agent.mutate()

    def __str__(self):
        return 'Population of {}\n'.format(self.population) + '\n'.join([x.__str__() for x in self.agents])
