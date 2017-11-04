import math
import matplotlib.pyplot as plt
import numpy as np


# This function returns the euclidean distance between the two given points
def distance(p1, p2):
    summation = 0.0
    for i in range(len(p1)):
        summation += (p1[i] - p2[i]) ** 2
    return math.sqrt(summation)


# Calculate the SSW
def get_ssw(data, centroids, labels):
    ssw = 0
    for i in range(len(data)):
        ssw += distance(data[i], centroids[labels[i]])
    return ssw


# Plots a set of results
def plot_results(results):
    for r in results:
        plt.title(r[0])
        plt.xlabel(r[1])
        plt.ylabel(r[3])
        plt.subplot(r[5])
        plt.plot(r[2], r[4])
    plt.show()
