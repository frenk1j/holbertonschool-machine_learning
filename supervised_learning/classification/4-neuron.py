#!/usr/bin/env python3
"""
Defines a single neuron performing binary classification
with private attributes, forward propagation, cost, and evaluation
"""

import numpy as np


class Neuron:
    """Single neuron for binary classification with private attributes"""

    def __init__(self, nx):
        """
        Initialize the neuron

        nx: number of input features
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for weights"""
        return self.__W

    @property
    def b(self):
        """Getter for bias"""
        return self.__b

    @property
    def A(self):
        """Getter for activated output"""
        return self.__A

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron
        X: numpy.ndarray of shape (nx, m) containing input data
        Updates __A with sigmoid activation
        Returns __A
        """
        z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-z))  # sigmoid
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost using binary cross-entropy

        Y: numpy.ndarray with shape (1, m) of correct labels
        A: numpy.ndarray with shape (1, m) of activated output
        Returns: cost (float)
        """
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A) +
                       (1 - Y) * np.log(1.0000001 - A)) / m
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neuron’s predictions

        X: numpy.ndarray of shape (nx, m) containing input data
        Y: numpy.ndarray of shape (1, m) containing correct labels

        Returns: prediction (numpy.ndarray) and cost (float)
        """
        A = self.forward_prop(X)
        prediction = np.where(A >= 0.5, 1, 0)
        cost = self.cost(Y, A)
        return prediction, cost
