import random

from classes import Perceptron

amount_of_neuron = [5, 3, 10]
inputs = [random.random(), random.random(), random.random(), random.random(), random.random()]
perceptron = Perceptron(amount_of_neuron, inputs)

perceptron.operate()

print(perceptron.output)