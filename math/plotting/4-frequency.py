#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """Plot a histogram of student scores for a project"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Create histogram with bins every 10 units and black edges
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')

    # Set labels and title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Set x-axis range
    plt.xlim(0, 100)

    # Set y-axis range to start from 0
    plt.ylim(0, plt.ylim()[1])

    # Display the plot
    plt.show()
