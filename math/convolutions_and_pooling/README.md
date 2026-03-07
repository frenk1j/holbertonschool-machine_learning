# 🖼️ Convolutions and Pooling — Holberton School

> *"A convolution is just a sliding window of learned features — the building block of every modern computer vision model."*

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
- [Tasks](#-tasks)
- [Core Concepts at a Glance](#-core-concepts-at-a-glance)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

Before building Convolutional Neural Networks, you need to understand **what convolutions and pooling actually do at the mathematical level**. This project implements every core operation from scratch using only **NumPy** — no `np.convolve`, no deep learning frameworks — applied directly to the **MNIST** dataset.

Starting from a simple valid convolution on grayscale images, the complexity grows through padding, strides, multi-channel inputs, multiple kernels, and finally pooling — the complete mathematical foundation of every CNN.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

- What is a **convolution**?
- What is **max pooling**? **Average pooling**?
- What is a **kernel / filter**?
- What is **padding**?
- What is **"same" padding**? **"valid" padding**?
- What is a **stride**?
- What are **channels**?
- How to perform a **convolution over an image**
- How to perform **max / average pooling** over an image

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import numpy as np` is allowed
- **`np.convolve` is NOT allowed**
- Maximum of **two `for` loops** per convolution function
- All files must be executable
- All files must end with a new line

---

## ✅ Tasks

### 🔵 Grayscale Convolutions

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **Valid Convolution** | Convolve grayscale images with no padding — output shrinks by `(kh-1, kw-1)` | 7/7 |
| 1 | **Same Convolution** | Convolve grayscale images with padding so output size equals input size | 7/7 |
| 2 | **Convolution with Padding** | Convolve grayscale images with custom padding `(ph, pw)` on all sides | 7/7 |
| 3 | **Strided Convolution** | Convolve grayscale images with custom stride `(sh, sw)` and padding mode | 8/8 |

### 🟢 Multi-Channel & Multi-Kernel Convolutions

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 4 | **Convolution with Channels** | Convolve images with multiple channels (e.g. RGB) using a 3D kernel | 8/8 |
| 5 | **Multiple Kernels** | Apply multiple kernels at once, producing a multi-channel output volume | 8/8 |

### 🟠 Pooling

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 6 | **Pooling** | Perform max or average pooling with custom kernel size and stride | 8/8 |

---

## 🔬 Core Concepts at a Glance

### Convolution Output Size
```
Valid:   output = (m, h - kh + 1, w - kw + 1)
Same:    output = (m, h, w)         # padding = (kh-1)/2, (kw-1)/2
Custom:  output = (m, (h + 2ph - kh) / sh + 1, (w + 2pw - kw) / sw + 1)
```

### Padding Types

| Mode | Output Size | Padding Added |
|------|------------|---------------|
| **Valid** | Smaller than input | None |
| **Same** | Equal to input | `ph = (kh - 1) / 2`, `pw = (kw - 1) / 2` |
| **Full** | Larger than input | `ph = kh - 1`, `pw = kw - 1` |

### Pooling vs. Convolution

| Operation | Learnable? | Purpose |
|-----------|-----------|---------|
| **Convolution** | ✅ Yes (kernel weights) | Feature extraction |
| **Max Pooling** | ❌ No | Spatial downsampling, keep dominant features |
| **Avg Pooling** | ❌ No | Spatial downsampling, smooth features |

### Convolution on a Single Image (Grayscale, Valid)
```python
for i in range(output_h):
    for j in range(output_w):
        output[img, i, j] = np.sum(
            images[img, i:i+kh, j:j+kw] * kernel
        )
```

---

## 📚 Resources

### Conceptual
- [Image Kernels](https://setosa.io/ev/image-kernels/)
- [Understanding Convolutional Layers](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)
- [A Comprehensive Guide to CNNs — the ELI5 way](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)
- [What is Max Pooling?](https://www.quora.com/What-is-max-pooling-in-convolutional-neural-networks)
- [Edge Detection Examples](https://www.youtube.com/watch?v=XuD4C8vJzEQ)
- [Padding](https://www.youtube.com/watch?v=smHa2442Ah4)
- [Strided Convolutions](https://www.youtube.com/watch?v=tQYZaDn_kSg)
- [Convolutions over Volumes](https://www.youtube.com/watch?v=KTB_OFoAQcc)
- [Pooling Layers](https://www.youtube.com/watch?v=8oOgPUO-TBY)

### References
- [`numpy.pad`](https://numpy.org/doc/stable/reference/generated/numpy.pad.html)
- [A Guide to Convolution Arithmetic for Deep Learning (paper)](https://arxiv.org/abs/1603.07285)
- [Convolution — Wikipedia](https://en.wikipedia.org/wiki/Convolution)
- [Kernel (image processing)](https://en.wikipedia.org/wiki/Kernel_(image_processing))

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── math/
    └── convolutions_and_pooling/
        ├── README.md
        ├── 0-convolve_grayscale_valid.py   # Valid convolution
        ├── 1-convolve_grayscale_same.py    # Same convolution
        ├── 2-convolve_grayscale_padding.py # Custom padding
        ├── 3-convolve_grayscale.py         # Strided convolution
        ├── 4-convolve_channels.py          # Multi-channel convolution
        ├── 5-convolve.py                   # Multiple kernels
        └── 6-pool.py                       # Max / average pooling
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*