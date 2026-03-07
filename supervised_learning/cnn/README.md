# 🧠 Convolutional Neural Networks — Holberton School

> *"Convolutions are the reason computers can finally see."*

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-FF6F00?style=flat-square&logo=tensorflow)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-013243?style=flat-square&logo=numpy)
![Style](https://img.shields.io/badge/Style-pycodestyle_2.11.1-orange?style=flat-square)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-purple?style=flat-square&logo=ubuntu)

---

## 📋 Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Requirements](#-requirements)
- [Tasks](#-tasks)
- [CNN Architecture at a Glance](#-cnn-architecture-at-a-glance)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

This project bridges the gap between raw convolution math and full **Convolutional Neural Networks (CNNs)**. Forward and backward propagation are implemented from scratch using **NumPy** for both convolutional and pooling layers — then a complete **LeNet-5** architecture is built and trained using **TensorFlow / Keras**.

Understanding CNNs at this depth — including backpropagation through pooling — is what separates engineers who use deep learning from those who truly understand it.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

- What is a **convolutional layer**?
- What is a **pooling layer**?
- **Forward propagation** over convolutional and pooling layers
- **Back propagation** over convolutional and pooling layers
- How to **build a CNN** using TensorFlow and Keras

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2** and **TensorFlow 2.15**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- No module imports unless otherwise noted (`numpy` allowed where specified)
- All files must be executable
- All files must end with a new line

---

## ✅ Tasks

### 🔵 From Scratch (NumPy)

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **Convolutional Forward Prop** | Forward pass through a convolutional layer with activation, padding, and stride | 8/8 |
| 1 | **Pooling Forward Prop** | Forward pass through a max or average pooling layer with custom kernel and stride | 8/8 |
| 2 | **Convolutional Back Prop** | Backpropagation through a convolutional layer — compute `dA_prev`, `dW`, `db` | 8/8 |
| 3 | **Pooling Back Prop** | Backpropagation through a pooling layer using max mask or average distribution | 8/8 |

### 🟢 TensorFlow / Keras

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 4 | **LeNet-5 (Keras)** | Build and train the classic LeNet-5 CNN architecture using `tf.keras` | 7/7 |
| 5 | **Summarize Like a Pro** | Use `model.summary()` to analyze a Keras CNN and answer structural questions | 11/11 |

---

## 🏗️ CNN Architecture at a Glance

### LeNet-5 Architecture (Task 4)
```
Input (m, 28, 28, 1)
      │
  Conv2D(6, 5×5, same) → tanh
      │
  AvgPool2D(2×2, stride=2)
      │
  Conv2D(16, 5×5, valid) → tanh
      │
  AvgPool2D(2×2, stride=2)
      │
  Flatten
      │
  Dense(120) → tanh
      │
  Dense(84) → tanh
      │
  Dense(10) → softmax
      │
  Output (m, 10)
```

### Forward Propagation Through a Conv Layer
```
for h in range(output_h):
    for w in range(output_w):
        for c in range(c_new):
            Z[m, h, w, c] = sum(A_prev_slice * W[:,:,:,c]) + b[:,:,:,c]
A = activation(Z)
```

### Backprop Key Gradients
```
dA_prev  — gradient flowing back to the previous layer
dW       — gradient for kernel weight update
db       — gradient for bias update
```

### Pooling Backprop
| Pool Type | Backward Rule |
|-----------|--------------|
| **Max** | Gradient flows only to the position of the max value (mask) |
| **Average** | Gradient is distributed equally across all positions in the window |

---

## 📚 Resources

### Conceptual
- [Convolutional Neural Network — Wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network)
- [CNNs Explained](https://www.youtube.com/watch?v=YRhxdVk_sIs)
- [The Best Explanation of CNNs on the Internet](https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721)
- [Machine Learning is Fun! Part 3: Deep Learning and CNNs](https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721)
- [CNNs: The Biologically-Inspired Model](http://www.wildml.com/2015/11/understanding-convolutional-neural-networks-for-nlp/)
- [Back Propagation in CNNs — Intuition and Code](https://towardsdatascience.com/backpropagation-in-a-convolutional-layer-57e9de3fb84)
- [Backpropagation in a Convolutional Layer](https://pavisj.medium.com/convolutions-and-backpropagations-46026a8f5d2c)
- [CNN – Backward Propagation of the Pooling Layers](https://lanstonchu.wordpress.com/2018/09/01/convolutional-neural-network-cnn-backward-propagation-of-the-pooling-layers/)

### deeplearning.ai Videos
- [Why Convolutions](https://www.youtube.com/watch?v=ay3zYUeuyhU)
- [One Layer of a Convolutional Net](https://www.youtube.com/watch?v=jPOAS7uCODQ)
- [Simple Convolutional Network Example](https://www.youtube.com/watch?v=3PyJA9afwHk)
- [CNN Example](https://www.youtube.com/watch?v=bXJx7y51cl0)

### Papers & References
- [Gradient-Based Learning Applied to Document Recognition — LeNet-5](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)
- [`tf.keras.layers.Conv2D`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D)
- [`tf.keras.layers.AveragePooling2D`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/AveragePooling2D)
- [`tf.keras.layers.MaxPooling2D`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPooling2D)
- [`tf.keras.layers.Flatten`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten)
- [Reproducibility in Keras Models](https://keras.io/getting_started/faq/#how-can-i-obtain-reproducible-results-using-keras-during-development)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── supervised_learning/
    └── cnn/
        ├── README.md
        ├── 0-conv_forward.py       # Conv layer forward prop (NumPy)
        ├── 1-pool_forward.py       # Pooling forward prop (NumPy)
        ├── 2-conv_backward.py      # Conv layer backprop (NumPy)
        ├── 3-pool_backward.py      # Pooling backprop (NumPy)
        ├── 4-lenet5.py             # LeNet-5 in Keras
        └── 5-summarize.py          # Model summary analysis
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*