from GeneticAlgorithm.Network import Network
from GeneticAlgorithm.Models.StringModel import StringModel


def main():
    myNet = Network()
    myNet.create(20, 0.4, StringModel)

    for x in range(2000):
        print('Generation', x)
        # print('\nStart\n', myNet)
        myNet.evaluate()
        # print('\nEvaluated\n', myNet)
        myNet.selection()
        # print('\nSelected\n', myNet)
        myNet.crossover()
        # print('\nCrossed\n', myNet)
        myNet.mutate()
        # print('\nMutated\n', myNet)

    myNet.evaluate()
    print('\nResult\n', myNet)

if __name__ == '__main__':
    main()
