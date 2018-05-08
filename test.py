from GeneticAlgorithm.Network import Network
from GeneticAlgorithm.Models.StringModel import StringModel


def main():
    myNet = Network()
    myNet.create(100, 0.4, StringModel, 90)

    for x in range(200):
        print('Generation', x, myNet.getTopFitness())
        myNet.evaluate()
        myNet.selection()
        myNet.crossover()
        myNet.mutate()

        if(myNet.goalReached()):
            break

    myNet.evaluate()
    myNet.sort()
    print('\nResult\n', myNet)


if __name__ == '__main__':
    main()
