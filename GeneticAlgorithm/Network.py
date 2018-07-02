import random


class Network:
    def __init__(self):
        self.population = 0
        self.agents = []

    def create(self, population, num, model, goal):
        self.population = population
        self.model = model
        self.num = num
        self.goal = goal

        for _ in range(self.population):
            input = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            agent = self.model(len(input))
            agent.setInput(input)
            agent.initialize()

            self.agents.append(agent)

    def evaluate(self):
        for agent in self.agents:
            agent.evaluate()

    def selection(self):
        self.sort()
        self.agents = self.agents[:int(self.num * len(self.agents))]

    def sort(self):
        self.agents = sorted(self.agents, key=lambda agent: agent.fitness, reverse=True)

    def crossover(self):
        siblings = []
        for _ in range(int((self.population - len(self.agents)) / 2)):
            parent1 = random.choice(self.agents)
            parent2 = random.choice(self.agents)

            splitPoint = random.randint(0, parent1.length - 1)

            child1 = self.model(parent1.length)
            child1.setInput(parent1.inputString)

            child2 = self.model(parent1.length)
            child2.setInput(parent1.inputString)

            splitPoint1 = random.randint(0, parent1.length - 1)
            splitPoint2 = random.randint(0, parent1.length - 1)

            if(splitPoint1 > splitPoint2):
                splitPoint1, splitPoint2 = splitPoint2, splitPoint1
            
            child1.data = parent1.data[0:splitPoint1] + parent2.data[splitPoint1:splitPoint2] + parent1.data[splitPoint2:]
            child2.data = parent2.data[0:splitPoint1] + parent1.data[splitPoint1:splitPoint2] + parent2.data[splitPoint2:]

            print(child1.data, child2.data)

            siblings.append(child1)
            siblings.append(child2)

        self.agents.extend(siblings)

    def mutate(self):
        for agent in self.agents:
            agent.mutate()

    def getTopFitness(self):
        return max([x.fitness for x in self.agents])

    def goalReached(self):
        return self.getTopFitness() >= self.goal

    def __str__(self):
        topAgent = self.agents[0]
#        return 'Population of {}\n'.format(self.population) + '\n'.join([x.__str__() for x in self.agents])
        return topAgent.data + ', ' + str(topAgent.fitness)
