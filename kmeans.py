import numpy as np
import importFile as file
from utils import *


def kmeans(data, k):
    # Randomly choose clusters
    rng = np.random.RandomState( 2 )
    i = rng.permutation( data.shape[0] )[:k]
    centroids = data[i]
    clusters = [None] * len(data)
    new_clusters = [None] * len(data)

    converged = False
    while not converged:
        # Assign clusters based on closest centroid
        for i, d in enumerate( data ):
            best_distance = float( "inf" )
            best_centroid = -1
            # Find new centroids from minimum distance
            for j, c in enumerate( centroids ):
                dis_c = distance( d, c )
                if dis_c < best_distance:
                    best_distance = dis_c
                    best_centroid = j
            new_clusters[i] = best_centroid
        # Compute the new centroids
        centroids = np.zeros_like(centroids)
        cluster_len = np.zeros(k)
        for i, cl in enumerate(new_clusters):
            for j, value in enumerate(data[i]):
                centroids[cl][j] += value
            cluster_len[cl] += 1
        for i, centroid in enumerate(centroids):
            centroid[:] = [x / cluster_len[i] for x in centroid]
        # Check for convergence
        if np.array_equal( clusters, new_clusters ):
            converged = True
        clusters = new_clusters
    return (clusters, centroids)


(data, classif) = file.read_file("datasets/adult.arff")
(clusters, centroids) = kmeans(data, 2)
#print clusters