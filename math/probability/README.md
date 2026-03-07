# 🎲 Probability — Holberton School

> *"Probability is the very guide of life."* — Marcus Tullius Cicero

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Style](https://img.shields.io/badge/Style-pycodestyle_2.11.1-orange?style=flat-square)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-purple?style=flat-square&logo=ubuntu)

---

## 📋 Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Requirements](#-requirements)
- [Mathematical Approximations](#-mathematical-approximations)
- [Tasks](#-tasks)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

This project covers the fundamentals of **Probability Theory** as applied to Machine Learning and Data Science. From basic probability notation to common statistical distributions — Poisson, Exponential, Normal, and Binomial — each distribution is implemented **from scratch in Python**, without importing any external libraries.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

### Core Concepts
- What is **probability**?
- Basic **probability notation**
- What is **independence**? What is **disjoint**?
- What is a **union**? An **intersection**?
- General **addition** and **multiplication** rules

### Distributions
- What is a **probability distribution**?
- What is a **probability distribution function (PDF)**? A **probability mass function (PMF)**?
- What is a **cumulative distribution function (CDF)**?
- What is a **percentile**?
- What are **mean**, **standard deviation**, and **variance**?
- Common probability distributions

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- **No external module imports** unless otherwise specified
- All files must be executable
- All files must end with a new line

---

## 🔢 Mathematical Approximations

Since no libraries may be imported, the following constants and functions are used:

| Symbol | Approximation |
|--------|--------------|
| π (pi) | `3.1415926536` |
| e (Euler's number) | `2.7182818285` |
| erf(x) | `1 - (a1·t + a2·t² + a3·t³) · e^(-x²)` where `t = 1/(1 + 0.47047·x)` |

---

## ✅ Tasks

### 🟣 Poisson Distribution

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **Initialize Poisson** | Class constructor from data or given λ | 7/7 |
| 1 | **Poisson PMF** | Probability mass function for k occurrences | 8/8 |
| 2 | **Poisson CDF** | Cumulative distribution function up to k | 8/8 |

### 🔵 Exponential Distribution

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 3 | **Initialize Exponential** | Class constructor from data or given λ | 7/7 |
| 4 | **Exponential PDF** | Probability density function at x | 8/8 |
| 5 | **Exponential CDF** | Cumulative distribution function up to x | 8/8 |

### 🟢 Normal Distribution

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 6 | **Initialize Normal** | Class constructor from data or given μ and σ | 7/7 |
| 7 | **Normalize Normal** | Calculate z-score for a given x | 8/8 |
| 8 | **Normal PDF** | Probability density function at x | 8/8 |
| 9 | **Normal CDF** | Cumulative distribution function up to x | 8/8 |

### 🟠 Binomial Distribution

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 10 | **Initialize Binomial** | Class constructor from data or given n and p | 8/8 |
| 11 | **Binomial PMF** | Probability mass function for k successes | 8/8 |
| 12 | **Binomial CDF** | Cumulative distribution function up to k | 7/7 |

---

## 📚 Resources

### Probability Fundamentals
- [Probability — Wikipedia](https://en.wikipedia.org/wiki/Probability)
- [Basic Concepts](https://www.khanacademy.org/math/statistics-probability/probability-library)
- [Intro to Probability 1: Basic Notation](https://www.youtube.com/watch?v=SkidyDQuupA)
- [Intro to Probability 2: Independent and Disjoint](https://www.youtube.com/watch?v=GnWi526yBtk)
- [Intro to Probability 3: General Addition Rule; Union; OR](https://www.youtube.com/watch?v=TEnD0FDltRE)
- [Intro to Probability 4: General Multiplication Rule; Intersection; AND](https://www.youtube.com/watch?v=xSc4oLA9e8o)
- [Permutations and Combinations](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:prob-comb)

### Distributions & Statistics
- [Probability Distribution](https://en.wikipedia.org/wiki/Probability_distribution)
- [Probability Theory](https://en.wikipedia.org/wiki/Probability_theory)
- [Cumulative Distribution Functions](https://en.wikipedia.org/wiki/Cumulative_distribution_function)
- [Common Probability Distributions: The Data Scientist's Crib Sheet](https://medium.com/@srowen/common-probability-distributions-347e6b945ce4)
- [Normal Distribution & Empirical Rule](https://www.youtube.com/watch?v=mtH1fmUVkfE)
- [Variance](https://en.wikipedia.org/wiki/Variance)
- [Binomial Distribution](https://en.wikipedia.org/wiki/Binomial_distribution)
- [Poisson Distribution](https://en.wikipedia.org/wiki/Poisson_distribution)
- [Hypergeometric Distribution](https://en.wikipedia.org/wiki/Hypergeometric_distribution)

### NumPy References
- [`numpy.random.poisson`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.poisson.html)
- [`numpy.random.exponential`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html)
- [`numpy.random.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)
- [`numpy.random.binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.binomial.html)
- [`math.erf`](https://docs.python.org/3/library/math.html#math.erf)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── math/
    └── probability/
        ├── README.md
        ├── poisson.py       # Poisson distribution (tasks 0–2)
        ├── exponential.py   # Exponential distribution (tasks 3–5)
        ├── normal.py        # Normal distribution (tasks 6–9)
        └── binomial.py      # Binomial distribution (tasks 10–12)
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*