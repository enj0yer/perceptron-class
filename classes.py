
class Neuron:
    def __init__(self, value: float):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def calculate(self, neurons: list, weights: list[float]):
        acc = 0.0

        if len(neurons) != len(weights):
            raise AttributeError("Length's of neurons and weights are not same.")

        for neuron, weight in zip(neurons, weights):
            acc += neuron.value * weight

        acc /= len(neurons)
        self.__value = acc


class Layer:

    def __init__(self, neurons: list[Neuron], weights: list[list[float]]):
        self.__neurons = neurons
        self.__weights = weights

    @property
    def neurons(self):
        return self.__neurons

    @property
    def weights(self):
        return self.__weights


class Network:

    def __init__(self, layers: list[Layer]):
        self.__layers = layers

    @property
    def layers(self):
        return self.__layers

    def input_layer(self):
        return self.__layers[0]

    def output_layer(self):
        return self.__layers[-1]

    def train(self, iterations: int):
        for i in range(iterations):
            for layer in self.__layers:
                pass

    @staticmethod
    def vec_product(matrix1: list[float], matrix2: list[float]) -> float:
        return sum([float(x * y) for x, y in zip(matrix1, matrix2)])

    @staticmethod
    def matrix_transpose(mat: list[list[float]]) -> list[list[float]]:
        return [*map(list, zip(*mat))]

    @staticmethod
    def matrix_product(matrix1: list[list[float]], matrix2: list[list[float]]):
        l, n = len(matrix1), len(matrix2[0])
        ans = [[0.0 for i in range(n)] for j in range(l)]
        for i in range(l):
            for j in range(n):
                vec1 = matrix1[i]
                vec2 = Network.matrix_transpose(matrix2)[j]
                ans[i][j] = Network.vec_product(vec1, vec2)
        return ans
