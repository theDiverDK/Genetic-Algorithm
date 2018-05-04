from GeneticAlgorithm.Network import Network
from GeneticAlgorithm.Models.StringModel import StringModel


def main():
    myNet = Network()
    myNet.create(10, 0.2, StringModel)

    print(myNet)

    myNet.evaluate()
    myNet.selection()


if __name__ == '__main__':
    main()
