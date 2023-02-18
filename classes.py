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
        self.__weights = [[[(random.random() / 2 - 0.25) for k in range(self.__amount_of_neurons[i - 1])] for j in range(self.__amount_of_neurons[i])] for i in range(self.__amount_of_layers) if i != 0] if not weights else weights
        self.__states = [[0.0 for j in range(self.__amount_of_neurons[i])] for i in range(self.__amount_of_layers)]

        self.__init_input(inputs)

    def __init_input(self, inputs: list[float]):
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

    @property
    def weights(self) -> list[list[list[float]]]:
        return self.__weights

    @weights.setter
    def weights(self, _weights):
        self.__weights = _weights

    def operate(self, _input: list[float] = None):
        if _input:
            self.__init_input(_input)
        for i in range(1, self.__amount_of_layers):
            for j in range(self.__amount_of_neurons[i]):
                state = 0
                for k in range(self.__amount_of_neurons[i - 1]):
                    state += self.__states[i - 1][k] * self.__weights[i - 1][j][k]

                self.__states[i][j] = self.__activate(state)

    def __back_propagation(self):
        pass

    def study(self, inputs: list[list[float]], outputs: list[list[float]], epoches: int = 1):

        delta = [[0.0 for j in range(self.__amount_of_neurons[i] + 1)] for i in range(self.__amount_of_layers)]

        for i in range(epoches):
            rn = [j for j in range(len(inputs[0]))]

            img_index = 0
            for j in range(len(inputs)):
                img_index = rn[i]
                self.__init_input(inputs[j])
                self.operate()
                result = self.output

                for r in range(self.__amount_of_neurons[self.__amount_of_layers - 1]):
                    delta[self.__amount_of_layers - 1][r] = (self.__states[self.__amount_of_layers - 1][r] * (1 - self.__states[self.__amount_of_layers - 1][r])) * (outputs[img_index][r] - result[r])

                for w in range(self.__amount_of_neurons[self.__amount_of_layers - 2] + 1):
                    self.__weights[self.__amount_of_layers - 1][r][w] += self.__states[self.__amount_of_layers - 2][w] * delta[self.__amount_of_layers - 1][r]

                for t in range(self.__amount_of_layers - 2, 0, -1):
                    for r in range(1, self.__amount_of_neurons[t] + 1):
                        _sum = 0
                        for s in range(1, self.__amount_of_neurons[t + 1] + 1):
                            _sum += delta[t + 1][s] * self.__weights[t + 1][s][r]

                        delta[t][r] = _sum * self.__states[t][r] * (1 - self.__states[t][r])

                        for a in range(self.__amount_of_neurons[t - 1] + 1):
                            self.__weights[t][r][a] += self.__states[t - 1][a] * delta[t][r]

    def __str__(self):
        return self.output
