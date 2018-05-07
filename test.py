from GeneticAlgorithm.Network import Network
from GeneticAlgorithm.Models.StringModel import StringModel


def main():
    myNet = Network()
    myNet.create(10, 0.2, StringModel)


    for x in range(2):
        print('\nGeneration',x)
        myNet.evaluate()
        myNet.selection()
        print('\nBefore crossover',myNet)
        myNet.crossover()
        print('\nAfter crossover',myNet)

    
if __name__ == '__main__':
    main()
