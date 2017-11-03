import random
import numpy as np
import importFile as file


def kmeans(data, k, iterations):

    find_clusters(data, k)


def distance():
    return None


def find_clusters(data, k):
    # Randomly choose clusters
    rng = np.random.RandomState( 2 )
    i = rng.permutation( data.shape[0] )[:k]
    centroids = data[i]
    clusters = []
    new_clusters = []

    while True:
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
        # Check for convergence
        if np.all( clusters == new_clusters ):
            break
        clusters = new_clusters
    return clusters


data = file.read_file("datasets/adult.arff")
kmeans(data, 4, 100)