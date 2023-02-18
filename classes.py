import math
import random


class Perceptron:
    def __init__(self, amount_of_neurons: list[int], inputs: list[float] = None, weights: list[list[list[float]]] = None):
        self.__amount_of_layers = len(amount_of_neurons)
        self.__amount_of_neurons = amount_of_neurons
        self.__weights = None
        self.__states = None
        if inputs:
            self.__create(inputs, weights)

    def __create(self, inputs: list[float], weights: list[list[list[float]]]):
        self.__weights = [[[random.random() for k in range(self.__amount_of_neurons[i - 1])] for j in range(self.__amount_of_neurons[i])] for i in range(self.__amount_of_layers) if i != 0] if not weights else weights
        self.__states = [[0.0 for j in range(self.__amount_of_neurons[i])] for i in range(self.__amount_of_layers)]

        for i in range(len(inputs)):
            self.__states[0][i] = inputs[i]

    @staticmethod
    def __activate(value: float) -> float:
        return 1 / (1 + math.exp(-value))

    @property
    def input(self) -> list[float]:
        return self.__states[0]

    @input.setter
    def input(self, _input: list[float]):
        self.__states[0] = _input

    @property
    def output(self) -> list[float]:
        return self.__states[-1]

    def operate(self):
        for i in range(1, self.__amount_of_layers):
            for j in range(self.__amount_of_neurons[i]):
                state = 0
                for k in range(self.__amount_of_neurons[i - 1]):
                    print(i, j, k)
                    state += self.__states[i - 1][k] * self.__weights[i - 1][j][k]

                self.__states[i][j] = self.__activate(state)

    def __back_propagation(self):
        pass

    def study(self, inputs: list[list[float]], outputs: list[list[float]], epoches: int = 1):
        pass
