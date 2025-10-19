# Holberton School - Machine Learning: Linear Algebra Project

## Project Overview

This project is part of the **Holberton School Machine Learning curriculum** and focuses on **practical exercises in linear algebra using Python**.

The exercises cover vector and matrix manipulation, slicing lists, concatenation, element-wise operations, matrix multiplication, and other essential linear algebra tasks using both **Python lists** and **`numpy.ndarray`**.

The goal is to **practice mathematical concepts programmatically**, while following **Python best practices** (PEP8, no loops/conditionals when forbidden, documented functions, and clear code).

---

## Project Structure

The project contains **15 tasks (0–14)**, each implemented in a separate Python file:

| Task | File | Description |
|------|------|-------------|
| 0    | `0-slice_me_up.py` | Extract specific slices from a Python list. |
| 1    | `1-trim_me_down.py` | Extract middle columns from a 2D matrix using a single loop. |
| 2    | `2-size_me_please.py` | Determine the shape of nested Python lists. |
| 3    | `3-flip_me_over.py` | Transpose a 2D matrix. |
| 4    | `4-line_up.py` | Add two 1D lists element-wise. |
| 5    | `5-across_the_planes.py` | Add two 2D matrices element-wise. |
| 6    | `6-howdy_partner.py` | Concatenate two 1D lists. |
| 7    | `7-gettin_cozy.py` | Concatenate two 2D matrices along a given axis. |
| 8    | `8-ridin_bareback.py` | Multiply two 2D matrices. |
| 9    | `9-let_the_butcher_slice_it.py` | Extract specific rows, columns, and submatrices from a `numpy.ndarray`. |
| 10   | `10-ill_use_my_scale.py` | Determine the shape of a `numpy.ndarray`. |
| 11   | `11-the_western_exchange.py` | Transpose a `numpy.ndarray`, including high-dimensional matrices. |
| 12   | `12-bracin_the_elements.py` | Element-wise addition, subtraction, multiplication, and division of two `numpy.ndarray`s. |
| 13   | `13-cats_got_your_tongue.py` | Concatenate two `numpy.ndarray`s along a specific axis. |
| 14   | `14-saddle_up.py` | Matrix multiplication of `numpy.ndarray`s without loops or conditionals. |

---

## General Requirements

- All functions **must return a new copy** of lists/matrices, not references.
- **No loops or conditionals** when not allowed.
- Some tasks allow only one loop or none at all.
- All functions are **fully documented**.
- All files follow **PEP8 style guidelines**.
- **Expected outputs** are provided in each task's main file (`*_main.py`).

---

## Example Usage

For example, task 12 (`12-bracin_the_elements.py`):

```python
import numpy as np
from 12-bracin_the_elements import np_elementwise

mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])

add, sub, mul, div = np_elementwise(mat1, mat2)

print("Add:\n", add)
print("Sub:\n", sub)
print("Mul:\n", mul)
print("Div:\n", div)
