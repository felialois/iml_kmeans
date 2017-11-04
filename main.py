import importFile
import kmeans
import bisecting_kmeans
import fuzzyCmeans
import utils
from sklearn import metrics
import sys


def main(algorithm, data, cl_labels, min_k, max_k, max_iterations, epsilon):
    results = []
    silhouette = []
    chs = []
    membership, centroids, labels = [], [], []

    for c in range(min_k, max_k + 1):
        if algorithm == 'kmeans':
            labels, centroids = kmeans.kmeans(data, c)
        elif algorithm == 'bisecting_kmeans':
            labels, centroids = bisecting_kmeans.bisecting_kmeans(data, c)
        elif algorithm == 'fuzzy_cmeans':
            membership, centroids = fuzzyCmeans.execute(data, max_iterations, c, epsilon)
            labels = fuzzyCmeans.get_labels(len(data), membership)

        silhouette.append((c, metrics.silhouette_score(data, labels, metric='euclidean')))
        chs.append((c, metrics.calinski_harabaz_score(data, labels)))

    results.append(("Silhouette", "Cluster Number", zip(*silhouette)[0], "Silhouette", zip(*silhouette)[1], 211))
    results.append(("CHS", "Cluster Number", zip(*chs)[0], "CHS", zip(*chs)[1], 212))

    print(labels)
    utils.plot_results(results)


arguments = sys.argv
file_name = arguments[1]
class_name = arguments[2]
algorithm = arguments[3]
minimum_k = int(arguments[4])
maximum_k = int(arguments[5])
max_iter = int(arguments[6])
epsilon_ = float(arguments[7])

da, classif = importFile.read_file(file_name, class_name)
main(algorithm, da, classif, minimum_k, maximum_k, max_iter, epsilon_)