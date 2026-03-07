# 📊 Plotting — Holberton School

> *"A picture is worth a thousand words — and a good plot is worth a thousand data points."*

![Score](https://img.shields.io/badge/Score-100%25-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8.3-11557c?style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-1.25.2-013243?style=flat-square&logo=numpy)
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

This project introduces **data visualization** using **Matplotlib**, Python's core plotting library. From simple line graphs to multi-plot figures and stacked bar charts, each task builds practical skills for visually communicating data — an essential step in every Machine Learning workflow for exploring, analyzing, and presenting results.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain the following **without the help of Google**:

- What is a **plot**?
- What is a **scatter plot**? A **line graph**? A **bar graph**? A **histogram**?
- What is **Matplotlib**?
- How to **plot data** with Matplotlib
- How to **label** a plot (axes, title, legend)
- How to **scale** an axis (linear, logarithmic)
- How to plot **multiple datasets** at the same time

---

## ⚙️ Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **Python 3.9**
- Executed with **NumPy 1.25.2** and **Matplotlib 3.8.3**
- First line of all files: `#!/usr/bin/env python3`
- Code must follow **pycodestyle** style (version 2.11.1)
- All modules, classes, and functions must be documented
- **No external module imports** unless otherwise specified
- All files must be executable
- All files must end with a new line

---

## 📦 Installation

```bash
pip install --user matplotlib==3.8.3
pip install --user Pillow==10.3.0
sudo apt-get install python3-tk
```

To verify the installation:

```bash
pip list
```

---

## ✅ Tasks

| # | Title | Type | Description | Score |
|---|-------|------|-------------|-------|
| 0 | **Line Graph** | Line | Plot `y = x³` as a solid red line, x-axis from 0 to 10 | 8/8 |
| 1 | **Scatter** | Scatter | Plot men's height vs weight as magenta scatter points | 9/9 |
| 2 | **Change of Scale** | Line (log) | Plot exponential bacteria growth with a logarithmic y-axis | 10/10 |
| 3 | **Two is Better Than One** | Multi-line | Overlay two datasets (C-14 decay & Ra-226 decay) on one plot | 13/13 |
| 4 | **Frequency** | Histogram | Plot a histogram of student grades with bin width of 10 | 10/10 |
| 5 | **All in One** | Subplots | Combine all previous plots into a single 3×2 figure | 11/11 |
| 6 | **Stacking Bars** | Bar | Plot a stacked bar chart of fruit quantities per person | 12/12 |

---

## 🖼️ Plot Types Covered

| Plot Type | Matplotlib Function | Use Case |
|-----------|-------------------|----------|
| Line graph | `plt.plot()` | Trends over time / continuous data |
| Scatter plot | `plt.scatter()` | Relationships between two variables |
| Log-scale line | `plt.yscale('log')` | Exponential / wide-range data |
| Histogram | `plt.hist()` | Frequency distributions |
| Subplots | `plt.subplot2grid()` | Multiple plots in one figure |
| Stacked bar | `plt.bar()` | Part-to-whole comparisons |

---

## 📚 Resources

### Plot Types
- [Plot (graphics)](https://en.wikipedia.org/wiki/Plot_(graphics))
- [Scatter plot](https://en.wikipedia.org/wiki/Scatter_plot)
- [Line chart](https://en.wikipedia.org/wiki/Line_chart)
- [Bar chart](https://en.wikipedia.org/wiki/Bar_chart)
- [Histogram](https://en.wikipedia.org/wiki/Histogram)

### Matplotlib Documentation
- [Pyplot tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
- [matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
- [`plt.plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
- [`plt.scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
- [`plt.bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)
- [`plt.hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
- [`plt.xlabel()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html) / [`plt.ylabel()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)
- [`plt.title()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)
- [`plt.subplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html) / [`plt.subplot2grid()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html)
- [`plt.xlim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html) / [`plt.ylim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html)
- [`plt.xscale()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html) / [`plt.yscale()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html)
- [mplot3d tutorial](https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html)

---

## 🗂️ Repository Structure

```
holbertonschool-machine_learning/
└── math/
    └── plotting/
        ├── README.md
        ├── 0-line.py       # Line graph
        ├── 1-scatter.py    # Scatter plot
        ├── 2-change_scale.py  # Logarithmic scale
        ├── 3-two_is_better_than_one.py  # Multi-line plot
        ├── 4-frequency.py  # Histogram
        ├── 5-all_in_one.py # Subplot grid
        └── 6-bars.py       # Stacked bar chart
```

---

## 👤 Author

**Alexa Orrico** — *Software Engineer at Holberton School*

---

*Holberton School — Machine Learning Track*