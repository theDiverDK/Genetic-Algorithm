from GeneticAlgorithm.Network import Network
from GeneticAlgorithm.Models.StringModel import StringModel


def main():
    myNet = Network()
    myNet.create(10, StringModel)

    print(myNet)
    
    for agent in myNet.agents:
        print(agent)


if __name__ == '__main__':
    main()
