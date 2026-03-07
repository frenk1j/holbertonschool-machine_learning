# ⚙️ Optimization — Holberton School

> *"Premature optimization is the root of all evil — but the right optimization at the right time is pure gold."*

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
- [Optimization Algorithms at a Glance](#-optimization-algorithms-at-a-glance)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

Training a neural network is only half the battle — **optimization** is what makes it learn fast, generalize well, and converge reliably. This project covers the full spectrum of modern deep learning optimization techniques: data normalization, mini-batch gradient descent, momentum, RMSProp, Adam, learning rate decay, and batch normalization.

Each algorithm is first **implemented from scratch with NumPy**, then applied using **TensorFlow 2 / Keras** — bridging theory and practice in a complete optimization toolkit.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

### Fundamentals
- What is a **hyperparameter**?
- How and why do you **normalize** input data?
- What is a **saddle point**?

### Gradient Descent Variants
- What is **stochastic gradient descent**?
- What is **mini-batch gradient descent**?
- What is a **moving average**? How do you implement it?
- What is **gradient descent with momentum**? How do you implement it?
- What is **RMSProp**? How do you implement it?
- What is **Adam optimization**? How do you implement it?

### Advanced Techniques
- What is **learning rate decay**? How do you implement it?
- What is **batch normalization**? How do you implement it?

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2** and **TensorFlow 2.15**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import numpy as np` and/or `import tensorflow as tf` are allowed
- Do not import any module unless it is being used
- All files must be executable
- All files must end with a new line

---

## ✅ Tasks

### 📐 Data Preprocessing

| # | Title | Tool | Description | Score |
|---|-------|------|-------------|-------|
| 0 | **Normalization Constants** | NumPy | Calculate mean and standard deviation of each feature | 6/6 |
| 1 | **Normalize** | NumPy | Standardize a matrix using precomputed mean and std | 6/6 |
| 2 | **Shuffle Data** | NumPy | Shuffle data points in two matrices in the same order | 6/6 |
| 3 | **Mini-Batch** | NumPy | Create randomized mini-batches for gradient descent | 5/5 |

### 📈 Gradient Descent Optimizers *(from scratch)*

| # | Title | Tool | Description | Score |
|---|-------|------|-------------|-------|
| 4 | **Moving Average** | NumPy | Compute exponentially weighted moving average with bias correction | 6/6 |
| 5 | **Momentum** | NumPy | Implement gradient descent with momentum update step | 6/6 |
| 6 | **Momentum Upgraded** | TensorFlow | Create a `tf.keras.optimizers.SGD` optimizer with momentum | 6/6 |
| 7 | **RMSProp** | NumPy | Implement the RMSProp update step from scratch | 6/6 |
| 8 | **RMSProp Upgraded** | TensorFlow | Create a `tf.keras.optimizers.RMSprop` optimizer | 6/6 |
| 9 | **Adam** | NumPy | Implement the Adam optimization update step from scratch | 6/6 |
| 10 | **Adam Upgraded** | TensorFlow | Create a `tf.keras.optimizers.Adam` optimizer | 6/6 |

### 📉 Learning Rate Decay

| # | Title | Tool | Description | Score |
|---|-------|------|-------------|-------|
| 11 | **Learning Rate Decay** | NumPy | Implement inverse time decay learning rate schedule | 6/6 |
| 12 | **Learning Rate Decay Upgraded** | TensorFlow | Create an `InverseTimeDecay` learning rate schedule in Keras | 6/6 |

### 🔷 Batch Normalization

| # | Title | Tool | Description | Score |
|---|-------|------|-------------|-------|
| 13 | **Batch Normalization** | NumPy | Normalize a layer's inputs using batch mean and variance | 6/6 |
| 14 | **Batch Normalization Upgraded** | TensorFlow | Create a batch normalization layer using `tf.nn.batch_normalization` | 6/6 |

### 🏆 Capstone

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 15 | **If you can't explain it simply, you don't understand it well enough** | Build, train, and save an optimized model combining all learned techniques | 29/29 |

---

## 🔬 Optimization Algorithms at a Glance

| Algorithm | Key Idea | Strengths |
|-----------|----------|-----------|
| **SGD** | Update weights after each sample | Simple, memory-efficient |
| **Mini-Batch GD** | Update after small batches | Balances speed and stability |
| **Momentum** | Accumulate velocity in gradient direction | Reduces oscillations, faster convergence |
| **RMSProp** | Adapt learning rate per parameter using squared gradient average | Good for non-stationary problems |
| **Adam** | Combines Momentum + RMSProp with bias correction | Fast, robust, widely used |
| **Batch Norm** | Normalize layer inputs during training | Stabilizes training, allows higher learning rates |
| **LR Decay** | Reduce learning rate over time | Prevents overshooting near minimum |

### Adam Update Rule
```
vdW = β₁·vdW + (1 - β₁)·dW          # Momentum term
sdW = β₂·sdW + (1 - β₂)·dW²         # RMSProp term
vdW_c = vdW / (1 - β₁ᵗ)             # Bias correction
sdW_c = sdW / (1 - β₂ᵗ)             # Bias correction
W = W - α · vdW_c / (√sdW_c + ε)    # Parameter update
```

---

## 📚 Resources

### Conceptual
- [Hyperparameter (machine learning)](https://en.wikipedia.org/wiki/Hyperparameter_(machine_learning))
- [Feature Scaling — Why, How and When](https://medium.com/greyatom/why-how-and-when-to-scale-your-features-4b30ab09db5f)
- [Moving Average](https://en.wikipedia.org/wiki/Moving_average)
- [An Overview of Gradient Descent Optimization Algorithms](https://ruder.io/optimizing-gradient-descent/)
- [Mini-Batch Gradient Descent](https://machinelearningmastery.com/gentle-introduction-mini-batch-gradient-descent-configure-batch-size/)
- [SGD with Momentum](https://distill.pub/2017/momentum/)
- [Understanding RMSprop](https://towardsdatascience.com/understanding-rmsprop-faster-neural-network-learning-62e116fcf29a)
- [Adam Optimization Algorithm](https://arxiv.org/abs/1412.6980)
- [Learning Rate Schedules](https://towardsdatascience.com/learning-rate-schedules-and-adaptive-learning-rate-methods-for-deep-learning-2c8f433990d1)

### deeplearning.ai Videos
- [Normalizing Inputs](https://www.youtube.com/watch?v=FDCfw-YqWTE)
- [Mini-Batch Gradient Descent](https://www.youtube.com/watch?v=4qJaSmvhxi8)
- [Exponentially Weighted Averages](https://www.youtube.com/watch?v=lAq96T8FkTw)
- [Gradient Descent With Momentum](https://www.youtube.com/watch?v=k8fTYJPd3_I)
- [RMSProp](https://www.youtube.com/watch?v=_e-LFe_igno)
- [Adam Optimization Algorithm](https://www.youtube.com/watch?v=JXQT_vxqwIs)
- [Batch Normalization](https://www.youtube.com/watch?v=tNIpEZLv_eg)

### TensorFlow References
- [`tf.keras.optimizers.SGD`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/SGD)
- [`tf.keras.optimizers.RMSprop`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/RMSprop)
- [`tf.keras.optimizers.Adam`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam)
- [`tf.nn.batch_normalization`](https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization)
- [`tf.nn.moments`](https://www.tensorflow.org/api_docs/python/tf/nn/moments)
- [`tf.keras.optimizers.schedules.InverseTimeDecay`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/InverseTimeDecay)
- [`numpy.random.permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.permutation.html)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── supervised_learning/
    └── optimization/
        ├── README.md
        ├── 0-norm_constants.py          # Normalization constants
        ├── 1-normalize.py               # Normalize matrix
        ├── 2-shuffle_data.py            # Shuffle data
        ├── 3-mini_batch.py              # Mini-batch creation
        ├── 4-moving_average.py          # Moving average
        ├── 5-momentum.py                # Momentum (NumPy)
        ├── 6-momentum.py                # Momentum (TensorFlow)
        ├── 7-RMSProp.py                 # RMSProp (NumPy)
        ├── 8-RMSProp.py                 # RMSProp (TensorFlow)
        ├── 9-Adam.py                    # Adam (NumPy)
        ├── 10-Adam.py                   # Adam (TensorFlow)
        ├── 11-learning_rate_decay.py    # LR decay (NumPy)
        ├── 12-learning_rate_decay.py    # LR decay (TensorFlow)
        ├── 13-batch_norm.py             # Batch normalization (NumPy)
        ├── 14-batch_norm.py             # Batch normalization (TensorFlow)
        └── 15-model.py                  # Full optimized model
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*