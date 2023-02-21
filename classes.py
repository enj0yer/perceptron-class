import math
import random
from functools import reduce


class Perceptron:
    def __init__(self, neurons_quantity: list[int], inputs: list[float] = None, weights: list[list[list[float]]] = None):
        self.__layers_quantity = len(neurons_quantity)
        self.__neurons_quantity = neurons_quantity
        self.__weights = None
        self.__states = None
        if inputs:
            self.__create(inputs, weights)

    def __create(self, inputs: list[float], weights: list[list[list[float]]] = None):
        self.__create_states()
        if weights:
            self.__weights = weights
        else:
            self.__create_weights()
        self.__init_input(inputs)

    def __create_states(self, multiplier: float = None, summand: float = None):
        if not multiplier and not summand:
            self.__states = [[0.0 for j in range(self.__neurons_quantity[i])] for i in range(self.__layers_quantity)]
        else:
            self.__states = [[(random.random() * multiplier + summand) for j in range(self.__neurons_quantity[i])] for i in range(self.__layers_quantity)]

    def __create_weights(self, multiplier: float = 1.0, summand: float = 0.0):
        self.__weights = [[[(random.random() * multiplier + summand) for k in range(self.__neurons_quantity[i - 1])] for j in range(self.__neurons_quantity[i])] for i in range(self.__layers_quantity) if i != 0]

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
            self.__create(_input)
        for i in range(1, self.__layers_quantity):
            for j in range(self.__neurons_quantity[i]):
                state = 0
                for k in range(self.__neurons_quantity[i - 1]):
                    state += self.__states[i - 1][k] * self.__weights[i - 1][j][k]

                self.__states[i][j] = self.__activate(state)

    @staticmethod
    def __output_error(output: list[float], expected: list[float]):
        pass        

    def study(self, inputs: list[list[float]], outputs: list[list[float]], speed: float, moment: float, epoches: int = 1):
        assert len(inputs) == len(outputs), "Images quantity in inputs and outputs are not equal."
        for epoche in range(epoches):
            for image in range(len(inputs)):
                self.operate(inputs[image])
                curr_error = 0.0
                prev_error = 0.0
                for layer_index in range(self.__layers_quantity - 1, 1, -1):
                    curr_error = reduce(lambda acc, x: acc + x, [(waiting - actual) ** 2 for actual, waiting in zip(self.output, outputs[image])])
                    for neuron_index in range(self.__neurons_quantity[layer_index]):
                        for weight_index in range(self.__neurons_quantity[layer_index - 1]):
                            # TODO Доделать обучение, пользуясь данными этой статьи https://microtechnics.ru/obuchenie-nejronnyh-setej-obratnoe-rasprostranenie-oshibki/
                            self.__weights[layer_index - 1][neuron_index][weight_index] += -speed

    def __str__(self):
        return self.output.__str__()
