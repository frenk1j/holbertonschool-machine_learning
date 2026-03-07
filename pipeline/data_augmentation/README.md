# 🔄 Data Augmentation — Holberton School

> *"More data beats a clever algorithm, but better data beats more data."* — Peter Norvig

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-FF6F00?style=flat-square&logo=tensorflow)
![TF--Datasets](https://img.shields.io/badge/TF--Datasets-4.9.2-FF6F00?style=flat-square&logo=tensorflow)
![Style](https://img.shields.io/badge/Style-pycodestyle_2.11.1-orange?style=flat-square)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-purple?style=flat-square&logo=ubuntu)

---

## 📋 Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Tasks](#-tasks)
- [Augmentation Techniques at a Glance](#-augmentation-techniques-at-a-glance)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

Data is the fuel of deep learning — but collecting and labeling large datasets is expensive and time-consuming. **Data augmentation** is the technique of artificially expanding your training set by applying transformations to existing images, making models more robust and reducing overfitting.

This project implements a full suite of image augmentation operations using **TensorFlow's `tf.image` API**, applied to the **Stanford Dogs** dataset via `tensorflow-datasets`. The final task explores how **machine learning itself** can be used to automate the augmentation process.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

- What is **data augmentation**?
- **When** should you perform data augmentation?
- What are the **benefits** of using data augmentation?
- What are the various **ways to perform** data augmentation?
- How can you use **ML to automate** data augmentation?

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2** and **TensorFlow 2.15**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import tensorflow as tf` is allowed unless otherwise stated
- All files must be executable
- All files must end with a new line

---

## 📦 Installation

```bash
pip install --user tensorflow-datasets==4.9.2
```

---

## ✅ Tasks

| # | Title | Transform | `tf.image` Function | Score |
|---|-------|-----------|---------------------|-------|
| 0 | **Flip** | Horizontal mirror flip | `tf.image.flip_left_right` | 7/7 |
| 1 | **Crop** | Random crop to a given size | `tf.image.stateless_random_crop` | 7/7 |
| 2 | **Rotate** | Random rotation by 90° increments | `tf.image.rot90` | 7/7 |
| 3 | **Contrast** | Random contrast adjustment | `tf.image.stateless_random_contrast` | 7/7 |
| 4 | **Brightness** | Random brightness adjustment | `tf.image.stateless_random_brightness` | 7/7 |
| 5 | **Hue** | Random hue shift | `tf.image.stateless_random_hue` | 7/7 |
| 6 | **Automation** | Use AutoAugment-style ML to automate augmentation policy selection | — | 5/5 |

---

## 🔬 Augmentation Techniques at a Glance

| Technique | What It Does | Helps With |
|-----------|-------------|------------|
| **Flip** | Mirror image left-right | Orientation invariance |
| **Crop** | Random sub-region of image | Translation invariance, removes border dependency |
| **Rotate** | Rotate by random angle | Rotation invariance |
| **Contrast** | Randomly adjust contrast range | Lighting condition robustness |
| **Brightness** | Randomly shift pixel brightness | Exposure variation robustness |
| **Hue** | Randomly shift color hue | Color variation robustness |
| **AutoAugment** | ML-learned augmentation policies | Optimal task-specific augmentation |

### When to Augment
```
✅ Training set     → Always augment to increase diversity
❌ Validation set   → Never augment (need clean evaluation)
❌ Test set         → Never augment (need clean evaluation)
```

### Pipeline Example
```python
import tensorflow as tf

def augment(image, label):
    image = tf.image.flip_left_right(image)
    image = tf.image.random_brightness(image, max_delta=0.1)
    image = tf.image.random_contrast(image, lower=0.9, upper=1.1)
    return image, label

dataset = dataset.map(augment)
```

---

## 📚 Resources

- [Data Augmentation: Train Deep Learning Models with Less Data](https://nanonets.com/blog/data-augmentation-how-to-use-deep-learning-when-you-have-limited-data-part-2/)
- [A Complete Guide to Data Augmentation](https://www.v7labs.com/blog/data-augmentation-guide)
- [`tf.image` API Reference](https://www.tensorflow.org/api_docs/python/tf/image)
- [Data Augmentation — TensorFlow Tutorial](https://www.tensorflow.org/tutorials/images/data_augmentation)
- [Image Data Augmentation using TensorFlow](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomFlip)
- [Automating Data Augmentation: Practice, Theory and New Direction](https://ai.googleblog.com/2020/11/the-evolution-of-automl-and-learning-to.html)
- [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── pipeline/
    └── data_augmentation/
        ├── README.md
        ├── 0-flip.py          # Horizontal flip
        ├── 1-crop.py          # Random crop
        ├── 2-rotate.py        # Random rotation
        ├── 3-contrast.py      # Random contrast
        ├── 4-brightness.py    # Random brightness
        ├── 5-hue.py           # Random hue shift
        └── 6-autoaugment.py   # AutoAugment automation
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*