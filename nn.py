import numpy as np


class NeuralNetwork:

    def __init__(self, layer_sizes):

        self.W_L1 = np.random.normal(size=(layer_sizes[1], layer_sizes[0]))
        self.B_L1 = np.zeros((layer_sizes[1], 1))
        self.W_L2 = np.random.normal(size=(layer_sizes[2], layer_sizes[1]))
        self.B_L2 = np.zeros((layer_sizes[2], 1))
        self.y = 0
        # layer_sizes example: [4, 10, 2]

    def activation(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        z_L1 = np.matmul(self.W_L1, x) + self.B_L1
        a_L1 = self.activation(z_L1[0])
        z_L2 = np.matmul(self.W_L2, a_L1) + self.B_L2
        self.y = self.activation(z_L2[0])


'''
#test
this = NeuralNetwork([4, 10, 2])
this.forward(np.array([1, 2, 3, 4]))
print(this.y)
'''


