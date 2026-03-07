# 🔵 Clustering — Holberton School

> *"The goal is to turn data into information, and information into insight."* — Carly Fiorina

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-013243?style=flat-square&logo=numpy)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.5.0-f7931e?style=flat-square&logo=scikit-learn)
![SciPy](https://img.shields.io/badge/SciPy-1.11.4-8caae6?style=flat-square&logo=scipy)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-purple?style=flat-square&logo=ubuntu)

---

## 📋 Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Tasks](#-tasks)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

This project dives deep into **unsupervised learning** through the lens of **clustering** — one of the most fundamental techniques in Machine Learning. Starting from scratch implementations of **K-means** and **Gaussian Mixture Models (GMM)** with the Expectation-Maximization algorithm, to model selection with the **Bayesian Information Criterion** and **Hierarchical (Agglomerative) Clustering** with SciPy and Scikit-Learn.

Every core algorithm is first built from the ground up using only **NumPy**, then validated against industry-standard libraries.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

### Distributions & Clusters
- What is a **multimodal distribution**?
- What is a **cluster**? What is **cluster analysis**?
- What is **soft** vs **hard** clustering?

### K-Means
- What is **K-means clustering**?
- What is **cluster variance**?
- What is the **elbow / mountain method**?
- How to determine the **correct number of clusters**

### Gaussian Mixture Models
- What are **mixture models**?
- What is a **Gaussian Mixture Model (GMM)**?
- What is the **Expectation-Maximization (EM) algorithm**?
- How to implement the **EM algorithm for GMMs**
- What is the **Bayesian Information Criterion (BIC)**?

### Hierarchical Clustering
- What is **Hierarchical clustering**?
- What is **Agglomerative clustering**?
- What is **Ward's method**?
- What is **Cophenetic distance**?

### Libraries
- What is **scikit-learn**?
- What is **scipy**?

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2**, **Scikit-Learn 1.5.0**, and **SciPy 1.11.4**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import numpy as np` is allowed unless otherwise noted
- All files must be executable
- Code should use the **minimum number of operations**

---

## 📦 Installation

```bash
pip install --user scikit-learn==1.5.0
pip install --user scipy==1.11.4
```

---

## ✅ Tasks

### 🔵 K-Means Clustering *(from scratch)*

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **Initialize K-means** | Initialize cluster centroids using multivariate uniform distribution | 6/6 |
| 1 | **K-means** | Full K-means algorithm with convergence detection | 10/10 |
| 2 | **Variance** | Calculate total intra-cluster variance for a given set of centroids | 6/6 |
| 3 | **Optimize k** | Use the elbow method to find the optimal number of clusters | 10/10 |

### 🟢 Gaussian Mixture Models *(from scratch)*

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 4 | **Initialize GMM** | Initialize GMM parameters (priors, means, covariances) from K-means | 6/6 |
| 5 | **PDF** | Calculate the probability density function of a Gaussian distribution | 8/8 |
| 6 | **Expectation** | E-step: calculate posterior probabilities for each data point | 8/8 |
| 7 | **Maximization** | M-step: update GMM parameters from posterior probabilities | 6/6 |
| 8 | **EM** | Full Expectation-Maximization algorithm for GMMs | 12/12 |
| 9 | **BIC** | Find the optimal GMM using the Bayesian Information Criterion | 14/14 |

### 🟠 Scikit-Learn & SciPy

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 10 | **Hello, sklearn!** | K-means clustering using `sklearn.cluster.KMeans` | 4/4 |
| 11 | **GMM** | Gaussian Mixture Model using `sklearn.mixture.GaussianMixture` | 4/4 |
| 12 | **Agglomerative** | Hierarchical Agglomerative clustering with Ward linkage and dendrogram | 6/6 |

---

## 📚 Resources

### Conceptual
- [Understanding K-means Clustering in Machine Learning](https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1)
- [K-means clustering: how it works](https://www.youtube.com/watch?v=_aWzGGNrcic)
- [How many clusters? (Elbow Method)](https://www.youtube.com/watch?v=QXOkPvFM6NU)
- [Bimodal distribution](https://en.wikipedia.org/wiki/Multimodal_distribution)
- [Gaussian Mixture Model](https://en.wikipedia.org/wiki/Mixture_model#Gaussian_mixture_model)
- [EM algorithm: how it works](https://www.youtube.com/watch?v=REypj2sy_5U)
- [Expectation Maximization: how it works](https://www.youtube.com/watch?v=iQoXFmbXRJA)
- [Mixture Models 4: multivariate Gaussians](https://www.youtube.com/watch?v=JNlEIEwe-Cg)
- [Mixture Models 5: how many Gaussians?](https://www.youtube.com/watch?v=BWXd5dOkuTo)
- [What is Hierarchical Clustering?](https://www.youtube.com/watch?v=7xHsRkOdVwo)

### References
- [scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [sklearn.cluster.KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [sklearn.mixture.GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html)
- [scipy.cluster.hierarchy](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html)
- [scipy.cluster.hierarchy.linkage](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html)
- [scipy.cluster.hierarchy.fcluster](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html)
- [scipy.cluster.hierarchy.dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── unsupervised_learning/
    └── clustering/
        ├── README.md
        ├── 0-initialize.py       # K-means initialization
        ├── 1-kmeans.py           # K-means algorithm
        ├── 2-variance.py         # Intra-cluster variance
        ├── 3-optimum.py          # Elbow method / optimize k
        ├── 4-initialize.py       # GMM initialization
        ├── 5-pdf.py              # Gaussian PDF
        ├── 6-expectation.py      # EM E-step
        ├── 7-maximization.py     # EM M-step
        ├── 8-EM.py               # Full EM algorithm
        ├── 9-BIC.py              # Bayesian Information Criterion
        ├── 10-kmeans.py          # sklearn K-means
        ├── 11-gmm.py             # sklearn GMM
        └── 12-agglomerative.py   # SciPy hierarchical clustering
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*