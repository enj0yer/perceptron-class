
from classes import Perceptron

input_amount = 400
output_amount = 10

amount_of_neuron = [input_amount, 25, output_amount]
perceptron = Perceptron(amount_of_neuron)


perceptron.operate([(i + i) for i in range(input_amount)])

print(perceptron)
