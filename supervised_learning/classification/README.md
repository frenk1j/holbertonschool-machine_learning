# 🧠 Classification Using Neural Networks — Holberton School

> *"A neural network is a system that learns to do tasks by example, just as humans do."*

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-013243?style=flat-square&logo=numpy)
![Style](https://img.shields.io/badge/Style-pycodestyle_2.11.1-orange?style=flat-square)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-purple?style=flat-square&logo=ubuntu)

---

## 📋 Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Requirements](#-requirements)
- [Datasets](#-datasets)
- [Tasks](#-tasks)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

This project builds a **binary image classifier from scratch using only NumPy** — no deep learning frameworks. Starting from a single neuron performing logistic regression, the architecture grows progressively through a shallow neural network up to a full **deep neural network (DNN)** capable of **multiclass classification**.

Every core component — forward propagation, cost functions, backpropagation, gradient descent, and model persistence — is implemented manually, giving a deep understanding of how neural networks truly work under the hood.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

### Neural Network Fundamentals
- What is a **model**? What is **supervised learning**?
- What is a **prediction**? A **node**? A **weight**? A **bias**?
- What is a **layer**? A **hidden layer**?
- What is **Logistic Regression**?

### Activation Functions
| Function | When to Use |
|----------|-------------|
| **Sigmoid** σ(x) | Binary output layer |
| **Tanh** | Hidden layers (zero-centered) |
| **ReLU** | Deep hidden layers (avoids vanishing gradient) |
| **Softmax** | Multiclass output layer |

### Training
- What is a **loss function**? A **cost function**?
- What is **forward propagation**?
- What is **backpropagation**?
- What is **Gradient Descent**?
- What is a **Computation Graph**?
- How to **initialize weights and biases**
- The importance of **vectorization**
- How to **split your data** (train / dev / test)

### Multiclass Classification
- What is **multiclass classification**?
- What is a **one-hot vector**? How to encode/decode one-hot vectors?
- What is the **Softmax function** and when to use it?
- What is **cross-entropy loss**?
- What is **pickling** in Python?

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import numpy as np` is allowed unless otherwise noted
- **No loops** (`for`, `while`, etc.) unless otherwise noted
- All matrix multiplications must use `numpy.matmul`
- All files must be executable

---

## 📂 Datasets

| File | Description |
|------|-------------|
| `Binary_Train.npz` | Binary classification training set (hotdog / not hotdog images) |
| `Binary_Dev.npz` | Binary classification development/validation set |
| `MNIST.npz` | MNIST handwritten digits — keys: `X_train`, `Y_train`, `X_valid`, `Y_valid`, `X_test`, `Y_test` |

> Datasets should be stored in a separate `data/` directory. They are not uploaded to GitHub.

---

## ✅ Tasks

### 🔵 Single Neuron (Binary Classification)

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **Neuron** | Define a `Neuron` class with public attributes `W`, `b`, `A` | 7/7 |
| 1 | **Privatize Neuron** | Make `W`, `b`, `A` private with read-only getters | 6/6 |
| 2 | **Neuron Forward Propagation** | Implement sigmoid activation forward pass | 6/6 |
| 3 | **Neuron Cost** | Compute logistic regression (cross-entropy) cost | 6/6 |
| 4 | **Evaluate Neuron** | Return prediction and cost | 6/6 |
| 5 | **Neuron Gradient Descent** | Implement one step of gradient descent | 6/6 |
| 6 | **Train Neuron** | Full training loop with cost output | 13/13 |
| 7 | **Upgrade Train Neuron** | Add step-based cost printing and optional graph plotting | 14/14 |

### 🟢 Shallow Neural Network (One Hidden Layer)

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 8 | **NeuralNetwork** | Define a `NeuralNetwork` class with one hidden layer | 12/12 |
| 9 | **Privatize NeuralNetwork** | Make all attributes private with read-only getters | 6/6 |
| 10 | **NeuralNetwork Forward Propagation** | Implement sigmoid forward pass across two layers | 6/6 |
| 11 | **NeuralNetwork Cost** | Compute cross-entropy cost | 6/6 |
| 12 | **Evaluate NeuralNetwork** | Return predictions and cost | 6/6 |
| 13 | **NeuralNetwork Gradient Descent** | Backpropagation through two layers | 6/6 |
| 14 | **Train NeuralNetwork** | Full training loop | 13/13 |
| 15 | **Upgrade Train NeuralNetwork** | Add step-based printing and graph plotting | 14/14 |

### 🟠 Deep Neural Network (L Hidden Layers)

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 16 | **DeepNeuralNetwork** | Define a `DeepNeuralNetwork` class for L-layer networks | 13/13 |
| 17 | **Privatize DeepNeuralNetwork** | Make all attributes private with read-only getters | 6/6 |
| 18 | **DeepNeuralNetwork Forward Propagation** | Sigmoid forward pass through all L layers | 6/6 |
| 19 | **DeepNeuralNetwork Cost** | Compute cross-entropy cost | 6/6 |
| 20 | **Evaluate DeepNeuralNetwork** | Return predictions and cost | 6/6 |
| 21 | **DeepNeuralNetwork Gradient Descent** | Full backpropagation through L layers | 6/6 |
| 22 | **Train DeepNeuralNetwork** | Full training loop | 13/13 |
| 23 | **Upgrade Train DeepNeuralNetwork** | Add step-based printing and graph plotting | 14/14 |

### 🔴 Multiclass Classification & Utilities

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 24 | **One-Hot Encode** | Convert a label vector to a one-hot matrix | 22/22 |
| 25 | **One-Hot Decode** | Convert a one-hot matrix back to a label vector | 16/16 |
| 26 | **Persistence is Key** | Save and load model using `pickle` | 26/26 |
| 27 | **Update DeepNeuralNetwork** | Update DNN to support multiclass with Softmax output | 16/16 |
| 28 | **All the Activations** | Support sigmoid, tanh, ReLU, and softmax activations per layer | 20/20 |

---

## 🏗️ Architecture Overview

```
Input Layer (nx features)
       │
  ┌────▼────┐
  │ Hidden  │  × L layers — ReLU / Tanh activations
  │ Layers  │
  └────┬────┘
       │
  ┌────▼────┐
  │ Output  │  Sigmoid (binary) or Softmax (multiclass)
  │  Layer  │
  └─────────┘
       │
   Prediction
```

---

## 📚 Resources

### Fundamentals
- [Supervised vs. Unsupervised Machine Learning](https://www.ibm.com/think/topics/supervised-vs-unsupervised-learning)
- [What is a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk)
- [Forward Propagation](https://www.youtube.com/watch?v=MfIjxPh6Pys)
- [Understanding Activation Functions](https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0)
- [Loss Function](https://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html)
- [Gradient Descent](https://www.youtube.com/watch?v=IHZwWFHWa-w)
- [Backpropagation Calculus](https://www.youtube.com/watch?v=tIeHLnjs5U8)

### Classification
- [Binary Classification](https://www.youtube.com/watch?v=eqEc66RFY0I)
- [Logistic Regression](https://www.youtube.com/watch?v=hjrYrynGWGA)
- [Softmax Regression](https://www.youtube.com/watch?v=LLux1SW--oM)
- [Cross Entropy Loss](https://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html#cross-entropy)
- [What is One-Hot Encoding?](https://www.kaggle.com/code/dansbecker/using-categorical-data-with-one-hot-encoding)
- [Multiclass Classification](https://www.youtube.com/watch?v=ZvaELFv5IpM)

### Deep Networks
- [Deep L-Layer Neural Network](https://www.youtube.com/watch?v=2gw5tE2ziqA)
- [Random Initialization](https://www.youtube.com/watch?v=6by6Xas_Kho)
- [Initialization of Deep Networks](https://www.deeplearning.ai/ai-notes/initialization/)
- [Derivation: Derivatives for Common Activation Functions](https://towardsdatascience.com/deriving-backpropagation-with-cross-entropy-loss-d24811edeaf9)

### Python & NumPy
- [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)
- [`pickle`](https://docs.python.org/3/library/pickle.html)
- [What is Pickle in Python?](https://www.datacamp.com/tutorial/pickle-python-tutorial)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── supervised_learning/
    └── classification/
        ├── README.md
        ├── 0-neuron.py              # Neuron (public)
        ├── 1-neuron.py              # Neuron (private)
        ├── 2-neuron.py              # Forward propagation
        ├── 3-neuron.py              # Cost function
        ├── 4-neuron.py              # Evaluate
        ├── 5-neuron.py              # Gradient descent
        ├── 6-neuron.py              # Train
        ├── 7-neuron.py              # Upgrade train
        ├── 8-neural_network.py      # NeuralNetwork
        ├── 9-neural_network.py      # Privatize
        ├── 10-neural_network.py     # Forward propagation
        ├── 11-neural_network.py     # Cost
        ├── 12-neural_network.py     # Evaluate
        ├── 13-neural_network.py     # Gradient descent
        ├── 14-neural_network.py     # Train
        ├── 15-neural_network.py     # Upgrade train
        ├── 16-deep_neural_network.py  # DeepNeuralNetwork
        ├── 17-deep_neural_network.py  # Privatize
        ├── 18-deep_neural_network.py  # Forward propagation
        ├── 19-deep_neural_network.py  # Cost
        ├── 20-deep_neural_network.py  # Evaluate
        ├── 21-deep_neural_network.py  # Gradient descent
        ├── 22-deep_neural_network.py  # Train
        ├── 23-deep_neural_network.py  # Upgrade train
        ├── 24-one_hot_encode.py     # One-hot encode
        ├── 25-one_hot_decode.py     # One-hot decode
        ├── 26-deep_neural_network.py  # Persistence (pickle)
        ├── 27-deep_neural_network.py  # Multiclass update
        └── 28-deep_neural_network.py  # All activations
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*