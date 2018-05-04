from GeneticAlgorithm.Network import Network

from GeneticAlgorithm.StringModel import StringModel


def main():
    test = Network()
    test.create(10, StringModel)
    print(test)
    for agent in test.agents:
        print(agent)


if __name__ == '__main__':
    main()
