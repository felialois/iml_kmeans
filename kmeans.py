import random
import numpy as np
from importFile import readFile

file = "datasets/adult.arff"
data = readFile(file)
k = 3
centroids_coord = random.sample(range(0,len(data)),k)

print (centroids)

def kmeans(data, k, iterations):

    for i in range(0,iterations):
        pass


