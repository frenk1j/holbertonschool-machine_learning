# Calculus

This project is part of the **Holberton School Machine Learning** curriculum.  
It introduces key concepts of **calculus** through practical exercises using Python, including **summations**, **products**, **derivatives**, and **integrals**.

---

## 📚 Overview

Each task implements a mathematical concept programmatically or symbolically, helping to build a foundation for understanding optimization and analytical methods in machine learning.

---

## 🧩 Tasks Summary

| # | Task | Topic | File |
|---|------|--------|------|
| 0 | Sigma is for Sum | Basic summation | `0-sigma_is_for_sum` |
| 1 | The Greeks pronounce it sEEgma | Summation with expressions | `1-seegma` |
| 2 | Pi is for Product | Basic product notation | `2-pi_is_for_product` |
| 3 | The Greeks pronounce it pEE | Product with zero term | `3-pee` |
| 4 | Hello, derivatives! | Derivative of polynomial functions | `4-hello_derivatives` |
| 5 | A log on the fire | Derivative of xln(x) | `5-log_on_fire` |
| 6 | It is difficult to free fools... | Derivative of ln(x²) | `6-voltaire` |
| 7 | Partial truths... | Partial derivative of e^(xy) | `7-partial_truths` |
| 8 | Put it all together | Second partial derivatives | `8-all-together` |
| 9 | Our life is the sum total... | Summation of i² without loops | `9-sum_total.py` |
| 10 | Derive happiness... | Derivative of polynomial lists | `10-matisse.py` |
| 11 | Good grooming... | Basic integral of a polynomial | `11-integral` |
| 12 | We are all an integral part... | Exponential integration | `12-integral` |
| 13 | Create a definite plan... | Definite integrals | `13-definite` |
| 14 | My talents fall within... | Evaluating limits | `14-definite` |
| 15 | Winners are people... | Definite integral of constants | `15-definite` |
| 16 | Double whammy | Integration involving ln(2) | `16-double` |
| 17 | Integrate | Polynomial integral function | `17-integrate.py` |

---

## 🧮 Key Concepts

### ➕ Summations
Implemented using sigma notation and Python functions:
\[
\sum_{i=1}^{n} i^2
\]

### ✖️ Products
Explores pi notation:
\[
\prod_{i=1}^{m} i = m!
\]

### 🧠 Derivatives
Covers differentiation rules:
- Power rule
- Product rule
- Logarithmic differentiation
- Partial derivatives

### ∫ Integrals
Introduces:
- Indefinite and definite integrals
- Constant of integration `C`
- Integration of polynomials and exponentials

---

## ⚙️ Example
```python
from math import log

# Example: polynomial derivative
def poly_derivative(poly):
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    return [coef * i for i, coef in enumerate(poly)][1:]

print(poly_derivative([5, 3, 0, 1]))  # [3, 0, 3]
