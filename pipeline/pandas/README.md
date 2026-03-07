# 🐼 Pandas — Holberton School

> *"Without data, you're just another person with an opinion."* — W. Edwards Deming

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.2.2-150458?style=flat-square&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-013243?style=flat-square&logo=numpy)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-purple?style=flat-square&logo=ubuntu)

---

## 📋 Table of Contents

- [Description](#-description)
- [Learning Objectives](#-learning-objectives)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Datasets](#-datasets)
- [Tasks](#-tasks)
- [Resources](#-resources)
- [Author](#-author)

---

## 📖 Description

This project introduces **Pandas**, the essential Python library for data manipulation and analysis. Starting from creating DataFrames and loading real-world datasets, to slicing, merging, statistical analysis, and visualization — this project builds the practical data pipeline skills that are fundamental for any Machine Learning workflow.

The project uses real **cryptocurrency datasets** (Coinbase & Bitstamp) to apply these concepts in a realistic context.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

### Pandas Fundamentals
- What is **Pandas**?
- What is a **`pd.DataFrame`**? How do you create one?
- What is a **`pd.Series`**? How do you create one?
- How to **load data from a file**

### Data Manipulation
- How to perform **indexing** on a `pd.DataFrame`
- How to use **hierarchical indexing** with a `pd.DataFrame`
- How to **slice** a `pd.DataFrame`
- How to **reassign columns**
- How to **sort** a `pd.DataFrame`
- How to use **boolean logic** with a `pd.DataFrame`
- How to **merge / concatenate / join** `pd.DataFrames`

### Analysis & Visualization
- How to get **statistical information** from a `pd.DataFrame`
- How to **visualize** a `pd.DataFrame`

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2** and **Pandas 2.2.2**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- Only `import pandas as pd` is allowed unless otherwise noted
- All files must be executable
- All files must end with a new line

---

## 📦 Installation

```bash
pip install --user pandas==2.2.2
```

---

## 📊 Datasets

This project uses the **Coinbase** and **Bitstamp** cryptocurrency datasets, previously seen in the *Time Series Forecasting* project. These CSV files contain historical bitcoin price and volume data used for loading, cleaning, and analysis tasks.

---

## ✅ Tasks

### 🏗️ Creating DataFrames

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 0 | **From Numpy** | Create a `pd.DataFrame` from a `np.ndarray` with alphabetical column labels | 7/7 |
| 1 | **From Dictionary** | Create a `pd.DataFrame` from a predefined dictionary | 7/7 |
| 2 | **From File** | Load data into a `pd.DataFrame` from a CSV file | 7/7 |

### 🔧 Data Manipulation

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 3 | **Rename** | Rename columns and convert Unix timestamps to datetime | 7/7 |
| 4 | **To Numpy** | Select specific columns and convert to a `np.ndarray` | 7/7 |
| 5 | **Slice** | Slice rows and columns of a `pd.DataFrame` | 7/7 |
| 6 | **Flip it and Switch it** | Transpose and reverse a `pd.DataFrame` | 7/7 |
| 7 | **Sort** | Sort a `pd.DataFrame` in reverse chronological order | 7/7 |
| 8 | **Prune** | Remove rows with `NaN` values in a specific column | 7/7 |
| 9 | **Fill** | Fill missing values using forward/backward fill and column-specific values | 17/17 |

### 🔍 Indexing & Joining

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 10 | **Indexing** | Set the `Timestamp` column as the index | 7/7 |
| 11 | **Concat** | Concatenate two DataFrames with a hierarchical index | 12/12 |
| 12 | **Hierarchy** | Rearrange a MultiIndex `pd.DataFrame` | 7/7 |

### 📈 Analysis & Visualization

| # | Title | Description | Score |
|---|-------|-------------|-------|
| 13 | **Analyze** | Compute descriptive statistics for all columns | 7/7 |
| 14 | **Visualize** | Plot a `pd.DataFrame` as a candlestick/line chart | 22/22 |

---

## 📚 Resources

- [10 minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Complete Python Pandas Data Science Tutorial](https://www.youtube.com/watch?v=vmEHCJofslg) *(Reading CSV/Excel files, Sorting, Filtering, Groupby)*
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── pipeline/
    └── pandas/
        ├── README.md
        ├── 0-from_numpy.py      # DataFrame from ndarray
        ├── 1-from_dictionary.py # DataFrame from dictionary
        ├── 2-from_file.py       # DataFrame from CSV
        ├── 3-rename.py          # Rename columns
        ├── 4-array.py           # Convert to NumPy array
        ├── 5-slice.py           # Slice DataFrame
        ├── 6-flip_switch.py     # Transpose & reverse
        ├── 7-sort.py            # Sort rows
        ├── 8-prune.py           # Remove NaN rows
        ├── 9-fill.py            # Fill missing values
        ├── 10-index.py          # Set index
        ├── 11-concat.py         # Concatenate DataFrames
        ├── 12-hierarchy.py      # Hierarchical indexing
        ├── 13-analyze.py        # Descriptive statistics
        └── 14-visualize.py      # Visualization
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*