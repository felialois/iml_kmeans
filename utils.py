import cmath
import matplotlib.pyplot as plt


# This function returns the euclidean distance between the two given points
def distance(p1, p2):
    sumatory = 0
    for i in range(len(p1)):
        sumatory += (p1[i] - p2[i]) ^ 2
    return cmath.sqrt(sumatory)


# Plots a set of results
def plot_results(results):
    for r in results:
        plt.figure()
        plt.title(r[0])
        plt.xlabel(r[1])
        plt.ylabel(r[3])
        plt.plot(r[2], r[4])
    plt.show()