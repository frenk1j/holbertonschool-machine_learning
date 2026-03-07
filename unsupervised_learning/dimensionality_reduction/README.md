# 📉 Dimensionality Reduction — Holberton School

> *"The purpose of dimensionality reduction is not to discard information, but to find the most meaningful representation of it."*

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
- [Data](#-data)
- [Tasks](#-tasks)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

This project explores **Dimensionality Reduction** — the process of reducing the number of features in a dataset while preserving as much meaningful information as possible. Using only **NumPy**, two foundational techniques are implemented from scratch:

- **PCA (Principal Components Analysis)** — a linear method based on Singular Value Decomposition (SVD) that projects data onto the directions of maximum variance.
- **t-SNE (t-distributed Stochastic Neighbor Embedding)** — a non-linear technique ideal for visualizing high-dimensional data in 2D or 3D.

Both methods are applied to the **MNIST** handwritten digits dataset to reveal structure in high-dimensional data.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

### Linear Algebra Foundations
- What is **eigendecomposition**?
- What is **singular value decomposition (SVD)**?
- What is the difference between **eig** and **svd**?

### Dimensionality Reduction
- What is **dimensionality reduction** and what are its purposes?
- What is the difference between **linear** and **non-linear** dimensionality reduction?
- Which techniques are **linear** vs **non-linear**?

### Techniques
- What is **Principal Components Analysis (PCA)**?
- What is **t-distributed Stochastic Neighbor Embedding (t-SNE)**?
- What is a **manifold**?

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import numpy as np` is allowed unless otherwise noted
- All files must be executable
- Code should use the **minimum number of operations** to avoid floating point errors

---

## 📂 Data

The following MNIST dataset files are used to test the implementations:

| File | Description |
|------|-------------|
| `mnist2500_X.txt` | 2500 MNIST data points, each with 784 dimensions (28×28 pixels) |
| `mnist2500_labels.txt` | Corresponding digit labels (0–9) for each data point |

> ⚠️ **Note:** `np.ndarray`s are mutable objects. Slicing with `array[i]` returns a **view** (mutable), while `array[i, 0]` returns a **copy** (immutable). Be mindful when manipulating arrays in-place.

---

## ✅ Tasks

| # | Title | Method | Description | Score |
|---|-------|--------|-------------|-------|
| 0 | **PCA** | SVD (linear) | Compute the weights matrix `W` that maintains a given fraction of variance using SVD | 3/3 |
| 1 | **PCA v2** | SVD (linear) | PCA on a non-zero-mean dataset — centers the data before decomposition | 3/3 |

---

## 🔬 Techniques at a Glance

| Technique | Type | Key Idea | Best For |
|-----------|------|----------|----------|
| **PCA** | Linear | Projects onto directions of max variance via SVD | Preprocessing, noise reduction, visualization |
| **t-SNE** | Non-linear | Preserves local neighborhood structure on a manifold | 2D/3D visualization of high-dimensional clusters |

### PCA — How it works
```
1. Center the data: X = X - mean(X)
2. Compute SVD: X = U · Σ · Vᵀ
3. Select top nd components using cumulative explained variance
4. Return W = Vᵀ[:nd].T as the projection matrix
```

### t-SNE — How it works
```
1. Compute pairwise similarities in high-dimensional space (Gaussian kernel)
2. Compute pairwise similarities in low-dimensional space (Student t-distribution)
3. Minimize Kullback–Leibler divergence between the two distributions
4. Result: a 2D/3D embedding that preserves local structure
```

---

## 📚 Resources

### Conceptual
- [Dimensionality Reduction For Dummies — Part 1: Intuition](https://towardsdatascience.com/https-medium-com-abdullatif-h-dimensionality-reduction-for-dummies-part-1-a8c9ec7b7e79)
- [Singular Value Decomposition](https://www.youtube.com/watch?v=P5mlg91as1c)
- [Understanding SVD](https://towardsdatascience.com/understanding-singular-value-decomposition-and-its-application-in-data-science-388a54be95d)
- [Eigendecomposition vs SVD](https://math.stackexchange.com/questions/320220/intuitively-what-is-the-difference-between-eigendecomposition-and-singular-valu)
- [PCA Part 1](https://www.youtube.com/watch?v=FgakZw6K1QQ) / [PCA Part 2](https://www.youtube.com/watch?v=pVbMlzbeiRk)
- [StatQuest: t-SNE, Clearly Explained](https://www.youtube.com/watch?v=NEaUSP4YerM)
- [t-SNE tutorial Part 1](https://www.youtube.com/watch?v=ohkPU1jOyWY) / [Part 2](https://www.youtube.com/watch?v=1A8jDC2FGks)
- [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/)

### References
- [`numpy.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html)
- [Visualizing Data using t-SNE (paper)](https://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf)
- [Kullback–Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)
- [Manifold](https://en.wikipedia.org/wiki/Manifold)

### Advanced
- [Kernel PCA](https://en.wikipedia.org/wiki/Kernel_principal_component_analysis)
- [Nonlinear Dimensionality Reduction: KPCA](https://www.youtube.com/watch?v=HbDHohXPLnU)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── unsupervised_learning/
    └── dimensionality_reduction/
        ├── README.md
        ├── 0-pca.py          # PCA using SVD (zero-mean data)
        └── 1-pca.py          # PCA v2 (non-zero-mean data)
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*