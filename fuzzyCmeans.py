import numpy as np
import random
import importFile as file


def fuzzy_c_means(data, max_iterations, epsilon):
    c = 2


def execute(data, max_iterations, clusters):
    # Number of features
    features = len(data[0])
    # Number of rows
    rows = len(data)
    # create the first membership matrix
    u_matrix = []
    # fuzzy constant
    fc = 2.00

    for i in range(0, rows):
        vals = [random.random() for i in range(0, clusters)]
        s = sum(vals)
        memb = [v / s for v in vals]
        u_matrix.append(memb)

    # iteration counter
    iteration = 0

    while iteration < max_iterations:
        cntrs = get_centroids(data, u_matrix, clusters, fc)
        u_matrix = calculate_unity_matrix(cntrs, u_matrix, fc)
        iteration += 1

    return cntrs


def distance():
    return None


def get_centroids(data, membership, clusters, fuzzy_constant):
    centroids = []
    # Separate the memberships by cluster number
    mem = zip(*membership)

    for i in range(clusters):
        #  The cluster i memberships for every row
        mm = mem[i]
        # elevate every membership by the fuzzy constant
        mm_prod = [u ** fuzzy_constant for u in mm]
        denominator = sum(mm_prod)

        numerator = []
        # In every column calculate
        for j in range(len(data[0])):
            temp = []
            for k in range(len(data)):
                # uij**m * xi
                temp.append(mm_prod[k] * data[k][j])
            numerator.append(temp)

        numerator = [sum(x) for x in numerator]
        centroid = []
        # Calculate the centroid
        for n in numerator:
            centroid.append(n / denominator)
        centroids.append(centroid)

    return centroids


def calculate_unity_matrix(data, centroids, membership, fuzzy_constant):
    u_matrix = membership
    fc = 2 / (fuzzy_constant - 1)
    for i in range(len(data)):
        for k in range(len(centroids)):
            distances = map(distance, data[i], centroids[k])
            for l in range(len(centroids)):

    return None


d = file.read_file("datasets/adult.arff")
fuzzy_c_means(d, 100, 0.2)
