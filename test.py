from GeneticAlgorithm.Network import Network
from GeneticAlgorithm.Models.StringModel import StringModel


def main():
    myNet = Network()
    myNet.create(10, 0.2, StringModel)

    myNet.evaluate()
    myNet.selection()
    print(myNet)
    myNet.crossover()
    print('After crossover\n')
    print(myNet)

    
if __name__ == '__main__':
    main()
