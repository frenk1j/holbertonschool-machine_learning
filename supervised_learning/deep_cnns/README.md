# 🏛️ Deep Convolutional Architectures — Holberton School

> *"We need to go deeper."* — Inception (2010) & Every CNN Researcher Ever

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
- [Architectures at a Glance](#-architectures-at-a-glance)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

This project implements the landmark deep CNN architectures that transformed computer vision: **Inception (GoogLeNet)**, **ResNet-50**, and **DenseNet-121** — all built from scratch using **TensorFlow / Keras** by reading and replicating the original research papers.

Each architecture introduced a groundbreaking idea: Inception's parallel multi-scale convolutions, ResNet's skip connections that enabled training of 100+ layer networks, and DenseNet's dense connectivity that maximizes feature reuse. Mastering these architectures means being able to read any new paper and implement it directly.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

- What is a **skip connection**?
- What is a **bottleneck layer**?
- What is the **Inception Network**?
- What is **ResNet**? **ResNeXt**? **DenseNet**?
- How to **replicate a network architecture** by reading a journal article

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2** and **TensorFlow 2.15**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `from tensorflow import keras as K` is allowed
- All files must be executable
- All files must end with a new line

---

## ✅ Tasks

### 🟡 Inception Network (GoogLeNet — ILSVRC 2014 Winner)

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **Inception Block** | Build the parallel multi-branch inception module with 1×1, 3×3, 5×5 conv and max pool branches | 7/7 |
| 1 | **Inception Network** | Assemble the full GoogLeNet architecture using stacked inception blocks | 7/7 |

### 🔵 ResNet-50 (ILSVRC 2015 Winner)

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 2 | **Identity Block** | Build a residual identity block — skip connection when input and output dimensions match | 8/8 |
| 3 | **Projection Block** | Build a residual projection block — skip connection with 1×1 conv to match dimensions | 8/8 |
| 4 | **ResNet-50** | Assemble the full 50-layer ResNet using identity and projection blocks | 8/8 |

### 🟢 DenseNet-121

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 5 | **Dense Block** | Build a dense block where each layer receives feature maps from all preceding layers | 8/8 |
| 6 | **Transition Layer** | Build a transition layer that reduces spatial dimensions and channel count between dense blocks | 8/8 |
| 7 | **DenseNet-121** | Assemble the full DenseNet-121 architecture using dense blocks and transition layers | 8/8 |

---

## 🏗️ Architectures at a Glance

### Key Innovations Timeline

| Year | Architecture | Key Innovation | ILSVRC Result |
|------|-------------|---------------|---------------|
| 2014 | **GoogLeNet / Inception v1** | Parallel multi-scale convolutions (inception module) | 🥇 1st place |
| 2015 | **ResNet-50** | Skip connections / residual learning | 🥇 1st place |
| 2016 | **ResNeXt** | Grouped convolutions (aggregated residual transforms) | 🥈 1st runner-up |
| 2018 | **DenseNet-121** | Dense connectivity — every layer connects to every other layer | — |

---

### 🟡 Inception Block Structure
```
Input
 ├── Conv 1×1 (F1)                          → branch 1
 ├── Conv 1×1 (F3R) → Conv 3×3 (F3)        → branch 2
 ├── Conv 1×1 (F5R) → Conv 5×5 (F5)        → branch 3
 └── MaxPool 3×3    → Conv 1×1 (FPP)       → branch 4
          │
     Concatenate all branches
```

### 🔵 ResNet Residual Block Structure
```
Identity Block (same dims):          Projection Block (different dims):
  Input ──────────────────┐            Input ──── Conv 1×1 (stride=2) ──┐
    │                     │              │                               │
  Conv 1×1 → BN → ReLU    │            Conv 1×1 → BN → ReLU            │
    │                     │              │                               │
  Conv 3×3 → BN → ReLU    │            Conv 3×3 → BN → ReLU            │
    │                     │              │                               │
  Conv 1×1 → BN           │            Conv 1×1 → BN                   │
    │                     │              │                               │
   Add ←───────────────────┘           Add ←────────────────────────────┘
    │                                    │
   ReLU                                ReLU
```

### 🟢 DenseNet Dense Block
```
H₁ = F(x₀)
H₂ = F([x₀, H₁])
H₃ = F([x₀, H₁, H₂])
...
Hₙ = F([x₀, H₁, ..., Hₙ₋₁])   ← every layer sees ALL previous feature maps
```

---

## 📚 Resources

### Conceptual
- [Vanishing Gradient Problem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem)
- [1×1 Convolutions](https://www.youtube.com/watch?v=c1RBQzKsDCk)
- [What Does 1×1 Convolution Mean?](https://stats.stackexchange.com/questions/194142/what-does-1x1-convolution-mean-in-a-neural-network)
- [GoogLeNet Tutorial](https://www.youtube.com/watch?v=VxhSouuSZDY)
- [Review: GoogLeNet (Inception v1)](https://towardsdatascience.com/review-googlenet-inception-v1-winner-of-ilsvrc-2014-image-classification-c2b3565a64e7)
- [Residual Neural Network](https://en.wikipedia.org/wiki/Residual_neural_network)
- [An Overview of ResNet and its Variants](https://towardsdatascience.com/an-overview-of-resnet-and-its-variants-5281e2f56035)
- [Review: ResNet — Winner of ILSVRC 2015](https://towardsdatascience.com/review-resnet-winner-of-ilsvrc-2015-image-classification-localization-detection-e39402bfa5d8)
- [Review: ResNeXt — 1st Runner Up ILSVRC 2016](https://towardsdatascience.com/review-resnext-1st-runner-up-of-ilsvrc-2016-image-classification-15d7f17b42ac)
- [Review: DenseNet](https://towardsdatascience.com/review-densenet-image-classification-b6631a8ef803)
- [Network In Network](https://www.youtube.com/watch?v=c1RBQzKsDCk)
- [Inception Network Motivation](https://www.youtube.com/watch?v=C86ZXvgpejM)
- [Why ResNets Work](https://www.youtube.com/watch?v=RYth6EbBUqM)

### Original Papers
- [Network in Network (2014)](https://arxiv.org/abs/1312.4400)
- [Going Deeper with Convolutions — GoogLeNet (2014)](https://arxiv.org/abs/1409.4842)
- [Highway Networks (2015)](https://arxiv.org/abs/1505.00387)
- [Deep Residual Learning for Image Recognition — ResNet (2015)](https://arxiv.org/abs/1512.03385)
- [Aggregated Residual Transformations — ResNeXt (2017)](https://arxiv.org/abs/1611.05431)
- [Densely Connected Convolutional Networks — DenseNet (2018)](https://arxiv.org/abs/1608.06993)
- [Multi-Scale Dense Networks (2018)](https://arxiv.org/abs/1703.09844)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── supervised_learning/
    └── deep_cnns/
        ├── README.md
        ├── 0-inception_block.py    # Inception module
        ├── 1-inception_network.py  # GoogLeNet full architecture
        ├── 2-identity_block.py     # ResNet identity block
        ├── 3-projection_block.py   # ResNet projection block
        ├── 4-resnet50.py           # ResNet-50 full architecture
        ├── 5-dense_block.py        # DenseNet dense block
        ├── 6-transition_layer.py   # DenseNet transition layer
        └── 7-densenet121.py        # DenseNet-121 full architecture
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*