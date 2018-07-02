from GeneticAlgorithm.Models.StringModel import StringModel
from GeneticAlgorithm.Network import Network


def main():
    myNet = Network()
    myNet.create(200, 0.2, StringModel, 91)

    for x in range(10000):
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
