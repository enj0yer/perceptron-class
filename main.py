import random

from classes import Perceptron

input_amount = 400
output_amount = 10

amount_of_neuron = [input_amount, 25, output_amount]
perceptron = Perceptron(amount_of_neuron)

inputs = [[(i + j) for j in range(input_amount)] for i in range(20)]
outputs = [[(i * j) for j in range(output_amount)] for i in range(20)]

perceptron.study(inputs, outputs, 20)
perceptron.operate([(i + i) for i in range(input_amount)])

print(perceptron)