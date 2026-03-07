# 🛡️ Regularization — Holberton School

> *"Regularization is the art of finding the sweet spot between underfitting and overfitting."*

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
- [Regularization Techniques at a Glance](#-regularization-techniques-at-a-glance)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

Overfitting is one of the most common problems in deep learning — a model that memorizes the training data but fails to generalize. This project covers the most powerful **regularization techniques** used in modern neural networks: **L2 regularization**, **dropout**, **early stopping**, and **data augmentation**.

Each technique is implemented **from scratch with NumPy** to build deep intuition, then applied using **TensorFlow 2 / Keras** for production-ready usage.

> ⚠️ When initializing layer weights in TensorFlow tasks, use:
> `tf.keras.initializers.VarianceScaling(scale=2.0, mode="fan_avg")`

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

- What is **regularization**? What is its purpose?
- What are **L1** and **L2 regularization**? What is the difference between them?
- What is **dropout**?
- What is **early stopping**?
- What is **data augmentation**?
- How to implement each method in **NumPy** and **TensorFlow**?
- What are the **pros and cons** of each regularization method?

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2** and **TensorFlow 2.15**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import numpy as np` and/or `import tensorflow as tf` are allowed
- Do not import any module unless it is being used
- Weight initializer: `tf.keras.initializers.VarianceScaling(scale=2.0, mode="fan_avg")`
- All files must be executable
- All files must end with a new line

---

## ✅ Tasks

### 🔵 L2 Regularization *(Weight Decay)*

| # | Title | Tool | Description | Score |
|---|-------|------|-------------|-------|
| 0 | **L2 Regularization Cost** | NumPy | Add L2 penalty term to the network cost using Frobenius norm | 6/6 |
| 1 | **Gradient Descent with L2 Regularization** | NumPy | Update weights in backpropagation with L2 weight decay term | 6/6 |
| 2 | **L2 Regularization Cost** | TensorFlow | Compute L2 regularization cost from a TensorFlow neural network | 6/6 |
| 3 | **Create a Layer with L2 Regularization** | TensorFlow | Build a Dense layer with `tf.keras.regularizers.L2` applied | 6/6 |

### 🟢 Dropout Regularization

| # | Title | Tool | Description | Score |
|---|-------|------|-------------|-------|
| 4 | **Forward Propagation with Dropout** | NumPy | Implement dropout mask generation and forward pass | 6/6 |
| 5 | **Gradient Descent with Dropout** | NumPy | Backpropagate through a dropout-applied network | 6/6 |
| 6 | **Create a Layer with Dropout** | TensorFlow | Build a Dense layer followed by a `tf.keras.layers.Dropout` layer | 6/6 |

### 🟠 Early Stopping

| # | Title | Tool | Description | Score |
|---|-------|------|-------------|-------|
| 7 | **Early Stopping** | NumPy | Determine whether training should stop based on validation cost delta and patience | 10/10 |

### 🏆 Capstone

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 8 | **If you can't explain it to a six year old, you don't understand it yourself** | Build a fully regularized model combining L2, dropout, early stopping, and data augmentation | 22/22 |

---

## 🔬 Regularization Techniques at a Glance

| Technique | How It Works | Prevents | Trade-off |
|-----------|-------------|----------|-----------|
| **L1 Regularization** | Adds sum of absolute weights to cost | Overfitting; promotes sparsity | May zero out useful features |
| **L2 Regularization** | Adds sum of squared weights to cost | Overfitting; shrinks large weights | Slight increase in bias |
| **Dropout** | Randomly deactivates neurons during training | Co-adaptation of neurons | Slower convergence, non-deterministic |
| **Early Stopping** | Halts training when validation loss stops improving | Overfitting from over-training | May stop before optimal point |
| **Data Augmentation** | Artificially expands training set (flip, crop, rotate) | Overfitting from limited data | Increases training time |

### L2 Cost Formula
```
J_L2 = J + (λ / 2m) · Σ ||W||²_F

Where:
  J     = original cross-entropy cost
  λ     = regularization parameter (lambtha)
  m     = number of training examples
  ||W||²_F = Frobenius norm of the weight matrix
```

### Dropout Forward Pass
```
D = np.random.binomial(1, keep_prob, size=A.shape)  # Dropout mask
A = A * D                                            # Apply mask
A = A / keep_prob                                    # Inverted dropout scaling
```

---

## 📚 Resources

### Conceptual
- [Regularization (mathematics)](https://en.wikipedia.org/wiki/Regularization_(mathematics))
- [An Overview of Regularization Techniques in Deep Learning](https://www.analyticsvidhya.com/blog/2018/04/fundamentals-deep-learning-regularization-techniques/)
- [L2 Regularization and Back-Propagation](https://towardsdatascience.com/l2-regularization-and-back-propagation-bf9aef397e15)
- [Intuitions on L1 and L2 Regularisation](https://towardsdatascience.com/intuitions-on-l1-and-l2-regularisation-235f2db4c065)
- [Analysis of Dropout](https://pgaleone.eu/deep-learning/regularization/2017/01/10/anaysis-of-dropout/)
- [Early Stopping](https://en.wikipedia.org/wiki/Early_stopping)
- [How to Use Early Stopping Properly](https://towardsdatascience.com/early-stopping-a-cool-strategy-to-regularize-neural-networks-bfdeca6d722e)
- [Data Augmentation — How to Use Deep Learning with Limited Data](https://nanonets.com/blog/data-augmentation-how-to-use-deep-learning-when-you-have-limited-data-part-2/)

### deeplearning.ai Videos
- [Regularization](https://www.youtube.com/watch?v=6g0t3Phly2M)
- [Why Regularization Reduces Overfitting](https://www.youtube.com/watch?v=NyG-7nRpsW8)
- [Dropout Regularization](https://www.youtube.com/watch?v=D8PJAL-MZv8)
- [Understanding Dropout](https://www.youtube.com/watch?v=ARq74QuavAo)
- [Other Regularization Methods](https://www.youtube.com/watch?v=BOCLq2gpcGU)

### References
- [`numpy.linalg.norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)
- [`numpy.random.binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.binomial.html)
- [`tf.keras.regularizers.L2`](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L2)
- [`tf.keras.layers.Dense`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)
- [`tf.keras.layers.Dropout`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout)
- [Dropout: A Simple Way to Prevent Neural Networks from Overfitting (paper)](https://www.cs.toronto.edu/~rsalakhu/papers/srivastava14a.pdf)
- [Early Stopping — but when?](https://link.springer.com/chapter/10.1007/3-540-49430-8_3)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── supervised_learning/
    └── regularization/
        ├── README.md
        ├── 0-l2_reg_cost.py          # L2 cost (NumPy)
        ├── 1-l2_reg_gradient_descent.py  # L2 gradient descent (NumPy)
        ├── 2-l2_reg_cost.py          # L2 cost (TensorFlow)
        ├── 3-l2_reg_create_layer.py  # L2 layer (TensorFlow)
        ├── 4-dropout_forward_prop.py # Dropout forward pass (NumPy)
        ├── 5-dropout_gradient_descent.py  # Dropout backprop (NumPy)
        ├── 6-dropout_create_layer.py # Dropout layer (TensorFlow)
        ├── 7-early_stopping.py       # Early stopping logic
        └── 8-model.py                # Full regularized model
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*