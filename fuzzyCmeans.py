import math

import numpy as np
import utils


def execute(data, max_iterations, clusters, epsilon):
    # Number of features
    features = len(data[0])
    # Number of rows
    rows = len(data)
    # create the first membership matrix
    u_matrix = []
    # fuzzy constant
    fc = 2.00

    # create the membershipo metric using random numbers
    for i in range(rows):
        vals = np.random.rand(clusters)
        s = sum(vals)
        memb = [v / s for v in vals]
        u_matrix.append(memb)

    # iteration counter
    iteration = 0
    cntrs = []
    old_cntrs = []

    # Check if the number of iterations has reached the maximum or if the iterations have converged
    while (iteration < max_iterations) and (check_iteration(old_cntrs, cntrs, epsilon)):
        old_cntrs = cntrs
        # calcualte the Centroids
        cntrs = get_centroids(data, u_matrix, clusters, fc)
        # calculate the membership matrix
        u_matrix = calculate_membership_matrix(data, cntrs, u_matrix, fc)
        iteration += 1

    return u_matrix, cntrs


# Check if the iterations have converged
def check_iteration(c1, c2, epsilon):
    if not c1 or not c2:
        return True
    distances = [utils.distance(c1[i], c2[i]) for i in range(len(c1))]
    return not (np.amax(distances) < epsilon)


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
        # In every column calculate the ith centroid
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


# Calculate a new membership function using the centroids
def calculate_membership_matrix(data, centroids, membership, fuzzy_constant):
    u_matrix = membership
    fc = 2 / (fuzzy_constant - 1)
    for i in range(len(data)):
        # Calculate the distance of the row with the centroids
        distances = [utils.distance(data[i], centroids[k]) for k in range(len(centroids))]
        for k in range(len(centroids)):
            den = sum([math.pow(float(distances[k] / distances[c]), fc) for c in range(len(centroids))])
            u_matrix[i][k] = float(1 / den)
    return u_matrix


# Calculate which cluster is the one with the highest membership for every row
def get_labels(rows, membership):
    labels = []
    for i in range(rows):
        max_membership = -1
        max_mem_index = -1
        for j in range(len(membership[i])):
            if membership[i][j] > max_membership:
                max_membership = membership[i][j]
                max_mem_index = j
        labels.append(max_mem_index)
    return labels

