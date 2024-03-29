import importFile
import kmeans
import bisecting_kmeans
import fuzzyCmeans
import utils
from sklearn import metrics
import sys


def main(algorithm, data, cl_labels, min_k, max_k, max_iterations, epsilon):
    results, silhouette, chs, ssws, ssbs, ars, hom, comp = [], [], [], [], [], [], [], []
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
        ssws.append((c, utils.get_ssw(data, centroids, labels)))
        ssbs.append((c, utils.get_ssb(centroids)))
        ars.append((c, metrics.adjusted_rand_score(cl_labels, labels)))
        hom.append((c, metrics.homogeneity_score(cl_labels, labels)))
        comp.append((c, metrics.completeness_score(cl_labels, labels)))

    results.append(("Silhouette", "", zip(*silhouette)[0], "", zip(*silhouette)[1], 333, "blue"))
    results.append(("Calinski-Harabaz Index", "", zip(*chs)[0], "", zip(*chs)[1], 334, "blue"))
    results.append(("Intra cluster Variance", "", zip(*ssws)[0], "", zip(*ssws)[1], 331, "blue"))
    results.append(("Inter cluster Variance", "", zip(*ssbs)[0], "", zip(*ssbs)[1], 332, "blue"))
    results.append(("Adjusted Rand Index", "", zip(*ars)[0], "", zip(*ars)[1], 335, "orange"))
    results.append(("Homogeneity", "", zip(*hom)[0], "", zip(*hom)[1], 336, "orange"))
    results.append(("Completeness", "", zip(*comp)[0], "", zip(*comp)[1], 337, "orange"))

    print(labels)
    utils.plot_results(results, algorithm)


arguments = sys.argv
file_name = arguments[1]
class_name = arguments[2]
algo = arguments[3]
minimum_k = int(arguments[4])
maximum_k = int(arguments[5])
max_iter = int(arguments[6])
epsilon_ = float(arguments[7])

da, classif = importFile.read_file(file_name, class_name)
main(algo, da, classif, minimum_k, maximum_k, max_iter, epsilon_)
