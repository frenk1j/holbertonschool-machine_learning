# ⚡ TensorFlow 2 & Keras — Holberton School

> *"With Keras, you can go from idea to result in the shortest possible time."* — François Chollet

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-FF6F00?style=flat-square&logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-built--in-D00000?style=flat-square&logo=keras)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-013243?style=flat-square&logo=numpy)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-purple?style=flat-square&logo=ubuntu)

---

## 📋 Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Requirements](#-requirements)
- [Tasks](#-tasks)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

This project transitions from building neural networks from scratch to leveraging **TensorFlow 2** and its high-level API **Keras** (`tf.keras`). Every essential step of a production-ready ML workflow is covered: building models two different ways, adding regularization and dropout, compiling with optimizers and loss functions, training with callbacks (early stopping, learning rate decay), evaluating, saving, loading, and making predictions.

By the end, you'll have a complete and reusable deep learning pipeline built with industry-standard tools.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

### Keras & Models
- What is **Keras**?
- What is a **model**?
- How to instantiate a model (**2 ways**: Sequential API & Functional API)
- How to **build a layer**
- How to add **L2 regularization** to a layer
- How to add **dropout** to a layer
- How to add **batch normalization**

### Training Pipeline
- How to **compile** a model
- How to **optimize** a model
- How to **fit** a model
- How to use **validation data**
- How to perform **early stopping**
- How to measure **accuracy**

### Evaluation & Persistence
- How to **evaluate** a model
- How to **make a prediction** with a model
- How to **access weights/outputs** of a model
- What is **HDF5**?
- How to **save and load**:
  - A model's **weights**
  - A model's **configuration**
  - The **entire model**

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2** and **TensorFlow 2.15**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import tensorflow.keras as K` is allowed unless otherwise noted
- All files must be executable
- All files must end with a new line

---

## ✅ Tasks

### 🏗️ Building Models

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **Sequential** | Build a network using the `Sequential` API with L2 regularization and dropout | 7/7 |
| 1 | **Input** | Build the same network using the Functional API with the `Input` class | 7/7 |

### ⚙️ Compiling & Training

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 2 | **Optimize** | Compile a model with Adam optimizer, cross-entropy loss, and accuracy metric | 7/7 |
| 3 | **One Hot** | Convert labels to one-hot matrix using Keras utilities | 7/7 |
| 4 | **Train** | Train a model using `.fit()` and return the training history | 7/7 |
| 5 | **Validate** | Add validation data to the training loop | 7/7 |

### 🎛️ Callbacks

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 6 | **Early Stopping** | Create an early stopping callback monitoring validation loss | 7/7 |
| 7 | **Learning Rate Decay** | Create an inverse time decay learning rate scheduler callback | 7/7 |
| 8 | **Save Only the Best** | Create a ModelCheckpoint callback to save only the best model | 7/7 |

### 💾 Saving & Loading

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 9 | **Save and Load Model** | Save and reload an entire Keras model | 8/8 |
| 10 | **Save and Load Weights** | Save and reload only a model's weights | 8/8 |
| 11 | **Save and Load Configuration** | Save and reload a model's JSON configuration, then rebuild it | 13/13 |

### 📊 Evaluation & Prediction

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 12 | **Test** | Evaluate a model on test data and return loss and accuracy | 7/7 |
| 13 | **Predict** | Run inference and return predictions for a given dataset | 7/7 |

---

## 🔄 Keras Model Building: Two Ways

### 1️⃣ Sequential API
```python
import tensorflow.keras as K

model = K.Sequential()
model.add(K.layers.Dense(256, activation='tanh',
          kernel_regularizer=K.regularizers.L2(0.001)))
model.add(K.layers.Dropout(0.05))
model.add(K.layers.Dense(10, activation='softmax'))
```

### 2️⃣ Functional API
```python
inputs = K.Input(shape=(784,))
x = K.layers.Dense(256, activation='tanh',
    kernel_regularizer=K.regularizers.L2(0.001))(inputs)
x = K.layers.Dropout(0.05)(x)
outputs = K.layers.Dense(10, activation='softmax')(x)
model = K.Model(inputs=inputs, outputs=outputs)
```

---

## 📚 Resources

### Conceptual
- [TensorFlow 1 vs TensorFlow 2](https://www.youtube.com/watch?v=k5c-vg4rjBw)
- [Differences Between TF 1.x and TF 2.0](https://www.tensorflow.org/guide/migrate/tf1_vs_tf2)
- [Keras Explained](https://www.youtube.com/watch?v=qFJeN9V1ZsI)
- [Keras vs. tf.keras: What's the difference in TF 2.0?](https://pyimagesearch.com/2019/10/21/keras-vs-tf-keras-whats-the-difference-in-tensorflow-2-0/)
- [Hierarchical Data Format (HDF5)](https://en.wikipedia.org/wiki/Hierarchical_Data_Format)

### Official tf.keras API Reference
- [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
- [`tf.keras.models`](https://www.tensorflow.org/api_docs/python/tf/keras/models)
- [`tf.keras.layers`](https://www.tensorflow.org/api_docs/python/tf/keras/layers)
- [`tf.keras.activations`](https://www.tensorflow.org/api_docs/python/tf/keras/activations)
- [`tf.keras.callbacks`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks)
- [`tf.keras.initializers`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers)
- [`tf.keras.losses`](https://www.tensorflow.org/api_docs/python/tf/keras/losses)
- [`tf.keras.metrics`](https://www.tensorflow.org/api_docs/python/tf/keras/metrics)
- [`tf.keras.optimizers`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers)
- [`tf.keras.regularizers`](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers)
- [`tf.keras.utils`](https://www.tensorflow.org/api_docs/python/tf/keras/utils)
- [Serialization and Saving](https://www.tensorflow.org/guide/keras/serialization_and_saving)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── supervised_learning/
    └── keras/
        ├── README.md
        ├── 0-sequential.py        # Sequential API model
        ├── 1-input.py             # Functional API model
        ├── 2-optimize.py          # Compile model
        ├── 3-one_hot.py           # One-hot encoding
        ├── 4-train.py             # Basic training
        ├── 5-train.py             # Training with validation
        ├── 6-train.py             # Early stopping callback
        ├── 7-train.py             # Learning rate decay callback
        ├── 8-train.py             # Save best model callback
        ├── 9-model.py             # Save & load entire model
        ├── 10-weights.py          # Save & load weights
        ├── 11-config.py           # Save & load configuration
        ├── 12-test.py             # Evaluate model
        └── 13-predict.py          # Make predictions
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*