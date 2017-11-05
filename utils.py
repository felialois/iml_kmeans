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
    ssw = 0.0
    for i in range(len(data)):
        ssw += distance(data[i], centroids[labels[i]])
    return ssw / len(centroids)


# Calculate the SSB
def get_ssb(centroids):
    ssb = 0.0
    for i in range(len(centroids)):
        for j in range(len(centroids)):
            if i != j:
                ssb += math.pow(distance(centroids[i], centroids[j]),2)
    return (2 / float(len(centroids) * (len(centroids) - 1))) * ssb


# Plots a set of results
def plot_results(results, name):
    plt.figure(num=None, figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')
    plt.suptitle(name, fontsize=16)
    for r in results:
        plt.subplot(r[5])
        plt.xlabel(r[0])
        plt.plot(r[2], r[4], color=r[6])
    plt.show()
