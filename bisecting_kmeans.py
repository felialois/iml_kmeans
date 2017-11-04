import numpy as np
from utils import *
from kmeans import kmeans
from importFile import read_file


# This function calculates the score of a clustering
def mean_distance(data, bisect):
    (clusters, centroids) = bisect
    summation = 0.0
    for i, d in enumerate(data):
        summation += distance(d, centroids[clusters[i]])
    # We calculate the score with the inverse of the mean of the distances
    return summation / len(data)


def bisecting_kmeans(data, k):
    # Initially, we have to split all the data
    (clusters, centroids) = kmeans(data, 2)
    act_clusters = 2
    # We apply the bisecting step until we het the number of desired clusters k
    while act_clusters < k:
        best_mean_distance = -1
        best_class = (None, None)
        best_clustering = -1
        for i in range(act_clusters):
            # First we select the data in that cluster
            data_cluster = np.array([data[j] for j in range(len(data)) if clusters[j] == i])
            if len(data_cluster) > 1:
                # Now we must calculate the 2-means for every different cluster
                new_bisect = kmeans(data_cluster, 2)
                m_dist = mean_distance(data_cluster, new_bisect)
                # We look for the most heterogeneous cluster, the one with more mean distance
                if m_dist > best_mean_distance:
                    best_mean_distance = m_dist
                    best_class = new_bisect
                    best_clustering = i
        # Now we rearrange the classification
        k_cluster = 0
        for i in range(len(clusters)):
            if clusters[i] == best_clustering:
                # We must change the numbers of the actual clusters with the new information
                clusters[i] += best_class[0][k_cluster]
                k_cluster += 1
            elif clusters[i] > best_clustering:
                # We must increment in 1 the number of the cluster because we add 1 cluster
                clusters[i] += 1
                # Finally we replace the best cluster with the two generated
        new_centroids = []
        for i, c in enumerate(centroids):
            if i == best_clustering:
                new_centroids.extend(best_class[1])
            else:
                new_centroids.append(c)
        centroids = new_centroids
        act_clusters += 1
    # When we have the number of desired clusters we return the classification and the centroids
    return clusters, centroids

# (da, classif) = read_file("datasets/audiology.arff")
# (cl, cen) = bisecting_kmeans(da, 7)
# print cl
# print cen
