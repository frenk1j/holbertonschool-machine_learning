#!/usr/bin/env python3
"""
Defines a single neuron performing binary classification
with forward propagation, cost, evaluation, and gradient descent
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
        X: numpy.ndarray of shape (nx, m)
        Returns: __A
        """
        z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-z))
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost using binary cross-entropy
        """
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A) +
                       (1 - Y) * np.log(1.0000001 - A)) / m
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates predictions and returns prediction + cost
        """
        A = self.forward_prop(X)
        prediction = np.where(A >= 0.5, 1, 0)
        cost = self.cost(Y, A)
        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Performs one pass of gradient descent on the neuron

        X: input data, shape (nx, m)
        Y: correct labels, shape (1, m)
        A: activated output, shape (1, m)
        alpha: learning rate
        """
        m = Y.shape[1]
        dZ = A - Y
        dW = np.dot(dZ, X.T) / m
        db = np.sum(dZ) / m

        self.__W = self.__W - alpha * dW
        self.__b = self.__b - alpha * db
