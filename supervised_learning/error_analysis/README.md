# 🔍 Error Analysis — Holberton School

> *"Without data, you're just another person with an opinion. Without error analysis, you're just another person with a model."*

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
- [Key Metrics at a Glance](#-key-metrics-at-a-glance)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

A model that trains well but generalizes poorly is useless in production. This project covers the essential techniques for **diagnosing, quantifying, and reducing errors** in machine learning models. Starting from the **confusion matrix**, through precision, recall, F1 score, and up to **bias/variance analysis** and **Bayes error rate**, these tools are the foundation for understanding *why* a model fails — and *what to do about it*.

All metrics are implemented from scratch using only **NumPy**.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

### Confusion Matrix & Classification Metrics
- What is the **confusion matrix**?
- What is a **Type I error** (False Positive)? A **Type II error** (False Negative)?
- What is **sensitivity** (recall)? **Specificity**? **Precision**? **Recall**?
- What is the **F1 score**?

### Bias & Variance
- What is **bias**? **Variance**?
- What is **irreducible error**?
- What is **Bayes error**?
- How can you **approximate Bayes error**?
- How to **calculate bias and variance**
- How to **create a confusion matrix**

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import numpy as np` is allowed unless otherwise noted
- All files must be executable
- All files must end with a new line

---

## ✅ Tasks

### 📊 Confusion Matrix & Metrics

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **Create Confusion** | Build a confusion matrix from one-hot labels and predictions | 6/6 |
| 1 | **Sensitivity** | Calculate sensitivity (recall) for each class from a confusion matrix | 6/6 |
| 2 | **Precision** | Calculate precision for each class from a confusion matrix | 6/6 |
| 3 | **Specificity** | Calculate specificity for each class from a confusion matrix | 6/6 |
| 4 | **F1 Score** | Calculate F1 score for each class using sensitivity and precision | 6/6 |

### 🧠 Bias & Variance Analysis

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 5 | **Dealing with Error** | Determine the best strategy to reduce error given bias/variance analysis | 8/8 |
| 6 | **Compare and Contrast** | Answer questions comparing model performance, bias, and variance | 2/2 |

---

## 📐 Key Metrics at a Glance

### Confusion Matrix Structure

```
                    Predicted
                  Pos     Neg
Actual  Pos  │  TP   │  FN  │
        Neg  │  FP   │  TN  │
```

### Classification Metrics Formulas

| Metric | Formula | Measures |
|--------|---------|----------|
| **Sensitivity** (Recall) | TP / (TP + FN) | How well the model finds all positives |
| **Precision** | TP / (TP + FP) | How accurate positive predictions are |
| **Specificity** | TN / (TN + FP) | How well the model identifies negatives |
| **F1 Score** | 2 · (Precision · Recall) / (Precision + Recall) | Harmonic mean of precision and recall |

### Bias vs. Variance

| Condition | Diagnosis | Fix |
|-----------|-----------|-----|
| Train error ≈ Bayes error, Dev error >> Train error | **High Variance** | More data, regularization, dropout |
| Train error >> Bayes error | **High Bias** | Bigger network, more training, better architecture |
| Both train and dev error >> Bayes error | **High Bias + Variance** | Address bias first, then variance |
| Train error ≈ Dev error ≈ Bayes error | **Optimal** | — |

---

## 📚 Resources

### Classification Metrics
- [Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix)
- [Type I and Type II Errors](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors)
- [Sensitivity and Specificity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity)
- [Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall)
- [F1 Score](https://en.wikipedia.org/wiki/F-score)
- [What is a Confusion Matrix in Machine Learning?](https://machinelearningmastery.com/confusion-matrix-machine-learning/)
- [Simple Guide to Confusion Matrix Terminology](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)

### Bias & Variance
- [Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)
- [What is Bias and Variance?](https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229)
- [Bayes Error Rate](https://en.wikipedia.org/wiki/Bayes_error_rate)
- [What is Bayes Error in Machine Learning?](https://machinelearningmastery.com/bayes-error-rate/)
- [Bias/Variance (deeplearning.ai)](https://www.youtube.com/watch?v=SjQyLhQIXSM)
- [Basic Recipe for Machine Learning](https://www.youtube.com/watch?v=C1N_PDaawi0)
- [Why Human Level Performance](https://www.youtube.com/watch?v=J3HHOwcAR3o)
- [Avoidable Bias](https://www.youtube.com/watch?v=CZf3oo0fuh0)
- [Understanding Human-Level Performance](https://www.youtube.com/watch?v=r4nQBqlmBwM)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── supervised_learning/
    └── error_analysis/
        ├── README.md
        ├── 0-create_confusion.py   # Confusion matrix
        ├── 1-sensitivity.py        # Sensitivity / recall
        ├── 2-precision.py          # Precision
        ├── 3-specificity.py        # Specificity
        ├── 4-f1_score.py           # F1 score
        ├── 5-error_handling        # Bias/variance strategy (MCQ)
        └── 6-compare_and_contrast  # Compare models (MCQ)
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*