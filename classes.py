import math
import random


class Perceptron:
    def __init__(self, amount_of_neurons: list[int], inputs: list[float]):
        self.__amount_of_layers = len(amount_of_neurons)
        self.__amount_of_neurons = amount_of_neurons
        self.__weights = None
        self.__states = None
        self.__create(inputs)

    def __create(self, inputs: list[float]):
        self.__weights = [[[random.random() for k in range(self.__amount_of_neurons[i - 1])] for j in range(self.__amount_of_neurons[i])] for i in range(self.__amount_of_layers) if i != 0]
        self.__states = [[0.0 for j in range(self.__amount_of_neurons[i])] for i in range(self.__amount_of_layers)]

        for i in range(len(inputs)):
            self.__states[0][i] = inputs[i]

    @staticmethod
    def __activate(value: float) -> float:
        return 1 / (1 + math.exp(-value))

    @property
    def input(self) -> list[float]:
        return self.__states[0]

    @property
    def output(self) -> list[float]:
        return self.__states[-1]

    def operate(self):
        for i in range(1, self.__amount_of_layers):
            for j in range(self.__amount_of_neurons[i]):
                state = 0
                for k in range(self.__amount_of_neurons[i - 1]):
                    print(i, j, k)
                    state += self.__states[i - 1][k] * self.__weights[i][j][k]

                self.__states[i][j] = self.__activate(state)

