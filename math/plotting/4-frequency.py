#!/usr/bin/env python3
"""This module plots a histogram of student scores for a project."""

import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plots a histogram of student grades with bins every 10 units."""

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Create histogram
    plt.hist(student_grades, bins=10, range=(0, 100), edgecolor='black')

    # Set labels and title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Set x-axis range and ticks
    plt.xlim(0, 100)
    plt.xticks(range(0, 101, 10))

    # Display the plot
    plt.show()
