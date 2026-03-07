# 🔁 Transfer Learning — Holberton School

> *"Why train from scratch when giants have already learned to see?"*

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-FF6F00?style=flat-square&logo=tensorflow)
![CIFAR--10](https://img.shields.io/badge/Dataset-CIFAR--10-blue?style=flat-square)
![Accuracy](https://img.shields.io/badge/Validation_Accuracy-≥87%25-brightgreen?style=flat-square)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-purple?style=flat-square&logo=ubuntu)

---

## 📋 Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Requirements](#-requirements)
- [Tasks](#-tasks)
- [Transfer Learning Strategy](#-transfer-learning-strategy)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

Training a deep CNN from scratch requires massive datasets and compute. **Transfer learning** solves this by reusing the powerful feature representations learned by networks pre-trained on millions of images — and fine-tuning them for a new task with a fraction of the data and time.

This project applies transfer learning using **Keras Applications** (pre-trained models like VGG, ResNet, EfficientNet, etc.) to classify the **CIFAR-10** dataset, achieving **≥87% validation accuracy**. The key insight: freeze the pre-trained backbone, pre-compute its outputs once, and only train a lightweight classifier on top — saving enormous computation time.

A research blog post accompanies the implementation, documenting every experiment, hyperparameter choice, and lesson learned along the way.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

- What is **transfer learning**?
- What is **fine-tuning**?
- What is a **frozen layer**? How and **why** do you freeze a layer?
- How to use **transfer learning with Keras Applications**

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2** and **TensorFlow 2.15**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `from tensorflow import keras as K` is allowed unless otherwise noted
- Saved model must be named **`cifar10.h5`** and be compiled
- Model must achieve **≥ 87% validation accuracy** on CIFAR-10
- Script must **not run when imported**
- All files must be executable

---

## ✅ Tasks

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **Transfer Knowledge** | Train a CNN on CIFAR-10 using a Keras pre-trained application, achieving ≥87% validation accuracy. Includes `preprocess_data(X, Y)` function | 10/10 |
| 1 | **"Research is what I'm doing when I don't know what I'm doing."** | Blog post documenting the full experimental process: architectures tried, hyperparameters tuned, lessons learned | 12/12 |

---

## 🔬 Transfer Learning Strategy

### The 3-Step Process

```
Step 1 — Load Pre-trained Base
  base = K.applications.EfficientNetB0(
      weights='imagenet',
      include_top=False,        # Remove ImageNet classifier head
      input_shape=(224, 224, 3)
  )

Step 2 — Freeze the Base
  base.trainable = False        # Lock all pre-trained weights

Step 3 — Add Custom Classifier Head
  x = K.layers.GlobalAveragePooling2D()(base.output)
  x = K.layers.Dense(256, activation='relu')(x)
  output = K.layers.Dense(10, activation='softmax')(x)
  model = K.Model(inputs=base.input, outputs=output)
```

### CIFAR-10 Preprocessing Pipeline
```
CIFAR-10 images: (m, 32, 32, 3)
       │
  Lambda layer: tf.image.resize → (m, 224, 224, 3)   # Scale up for Keras apps
       │
  Application-specific preprocessing
  (e.g. K.applications.efficientnet.preprocess_input)
       │
  One-hot encode labels: (m,) → (m, 10)
```

### Key Optimization: Pre-compute Frozen Layer Outputs
```python
# Compute base model outputs ONCE — saves huge amounts of training time
features = base.predict(X_preprocessed)

# Only train the top layers on these precomputed features
top_model.fit(features, Y_one_hot, ...)
```

### Transfer Learning vs. Fine-tuning

| Strategy | Frozen Layers | Trainable Layers | When to Use |
|----------|--------------|-----------------|-------------|
| **Feature Extraction** | All base layers | New head only | Small dataset, similar domain |
| **Fine-tuning** | Bottom base layers | Top base + head | Larger dataset, slightly different domain |
| **Full Training** | None | All layers | Very large dataset |

---

## 📚 Resources

### Conceptual
- [A Comprehensive Hands-on Guide to Transfer Learning](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)
- [Transfer Learning — Wikipedia](https://en.wikipedia.org/wiki/Transfer_learning)
- [Transfer Learning & Fine-tuning (TF Tutorial)](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [A Survey on Deep Transfer Learning](https://arxiv.org/abs/1808.01974)

### References
- [Keras Applications (Pre-trained Models)](https://keras.io/api/applications/)
- [Keras Datasets](https://keras.io/api/datasets/)
- [`tf.keras.layers.Lambda`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Lambda)
- [`tf.image.resize`](https://www.tensorflow.org/api_docs/python/tf/image/resize)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── supervised_learning/
    └── transfer_learning/
        ├── README.md
        ├── 0-transfer.py      # Transfer learning script + preprocess_data()
        └── cifar10.h5         # Saved trained model (not pushed to GitHub)
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*