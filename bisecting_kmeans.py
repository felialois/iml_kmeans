import utils

def bisecting(data, k):
    # Initially, we have to split all the data
    (classif, centroids) = kmeans(data, 2)
    act_clusters = 2
    # We apply the bisecting step until we het the number of desired clusters k
    while act_clusters < act_clusters:
        best_score = 0
        best_class = (None, None)
        best_clustering = -1
        for i in range(act_clusters):
            # First we select the data in that cluster
            data_cluster = [data[j] for j in range(data) if classif[j] == i]
            # Now we must calculate the 2-means for every different cluster
            new_bisect = kmeans(data_cluster, 2)
            score = score(data_cluster, new_bisect)
            if score > best_score:
                best_score = score
                best_class = new_bisect
                best_clustering = i
        # Now we rearrange the classification
        for d_cluster in classif:
            # We must increment in 1 the number of the cluster because we add 1 cluster
            if d_cluster > best_clustering:
                d_cluster += 1
        # Finally we replace the best cluster with the two generated
        new_centroids = []
        for i,c in enumerate(centroids):
            if i == best_clustering:
                new_centroids.extend(new_bisect[1])
            else:
                new_centroids.append(c)
        centroids = new_centroids
    # When we have the number of desired clusters we return the classification and the centroids
    return (classif, centroids)

# This function calculates the score of a clustering
def score(data, bisect):
    (classif, centroids) = bisect
    sum = 0
    for i, d in enumerate(data):
        sum += distance(d, centroids[classif[i]])
    # We calculate the score with the inverse of the mean of the distances
    score = 1 / (sum / len(data))