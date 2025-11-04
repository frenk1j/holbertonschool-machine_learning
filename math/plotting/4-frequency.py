#!/usr/bin/env python3
"""This module plots a histogram of student scores for a project."""

import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plots a histogram of student grades with bins every 10 units."""

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Create histogram with bins every 10 units (0-100 range)
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')

    # Set labels and title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Set axis limits
    plt.xlim(0, 100)
    plt.ylim(0, 30)

    # Display the plot
    plt.show()
