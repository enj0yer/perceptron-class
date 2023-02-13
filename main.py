import random

from classes import Layer, Neuron

if __name__ == "__main__":

    layers_amount = 2
    neuron_amount = 3

    layers = [Layer([Neuron() for neuron in range(neuron_amount)], []) for layer in range(layers_amount)]
