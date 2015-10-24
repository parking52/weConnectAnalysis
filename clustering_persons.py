__author__ = 'melchior'
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift
from sklearn import metrics
import pickle
import pyjokes
from sklearn import datasets
from person import Person
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as scluchy

def getting_cluster_for_new_guy(new_guy):

    list_of_berlin_person = []
    list_of_newcomer_person = []

    if new_guy.type:  # newcomer

        list_of_berlin_person = pickle.load(open("berlin_persons.p", "rb"))
        list_of_berlin_person.append(new_guy)         # add the new guy
        list_of_person = list_of_berlin_person


    else:  # berliner

        list_of_newcomer_person = pickle.load(open("newcomer_persons.p", "rb"))
        list_of_newcomer_person.append(new_guy)        # add the new guy
        list_of_person = list_of_newcomer_person

    size_matrix = max(len(list_of_newcomer_person), len(list_of_berlin_person))

    matrix_to_compute = np.zeros(shape=(size_matrix, size_matrix))

    for i in range(size_matrix):
        for j in range(size_matrix):
            if i != j:
                matrix_to_compute[i][j] = (list_of_person[i].distance_of_two_persons(list_of_person[j]))
                # if j == size_matrix-1:
                #     print(matrix_to_compute[i][j])

    af = AffinityPropagation().fit(matrix_to_compute)
    ms = MeanShift().fit(matrix_to_compute)
    distArray = ssd.squareform(matrix_to_compute)
    linkage_matrix = scluchy.linkage(distArray, method='single', metric='euclidean')
    # output_tree = scluchy.to_tree(linkage_matrix, rd=True)

    labels = af.labels_
    labels = ms.labels_

    # print(linkage_matrix)
    print(labels)
    print(labels[-1]) ## label of the new guy

    indices_in_opposite_list = np.where(labels == labels[-1])[0]
    indices_in_opposite_list = indices_in_opposite_list[0:-1]  # remove last element which is the new guy

    refused_people = np.where(labels != labels[-1])[0]

    # if len(indices_in_opposite_list) < 5:
    if True:
        indices_in_opposite_list = matrix_to_compute[size_matrix-1].argsort()[-5:][::-1]
        print("not enough result going through fallback")

    refused_people = list(range(0, size_matrix-1))

    for value in indices_in_opposite_list:
        refused_people.remove(value)

    return indices_in_opposite_list, refused_people


if __name__ == '__main__':

    clusterer = AffinityPropagation()

    list_of_berlin_person = pickle.load(open("berlin_persons.p", "rb"))
    list_of_newcomer_person = pickle.load(open("newcomer_persons.p", "rb"))

    size_berlin = len(list_of_berlin_person)
    size_newcomers = len(list_of_newcomer_person)

    print(size_berlin)
    print(size_newcomers)

    centers = [[1, 1], [-1, -1], [1, -1]]
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    k_mean_4 = KMeans(n_clusters=4)


    matrix_berlin = np.zeros(shape=(size_berlin, size_berlin))
    matrix_newcomer = np.zeros(shape=(size_newcomers, size_newcomers))

    for i in range(size_berlin):
        for j in range(size_berlin):
            if i != j:
                matrix_berlin[i][j] = (list_of_berlin_person[i].distance_of_two_persons(list_of_berlin_person[j]))

    for i in range(size_newcomers):
        for j in range(size_newcomers):
            if i != j:
                matrix_newcomer[i][j] = (list_of_newcomer_person[i].distance_of_two_persons(list_of_newcomer_person[j]))

    print(matrix_berlin)
    print(matrix_newcomer)

    print('_____________________________________')
    clusterer.fit(matrix_newcomer, y=None)
    print('_____________________________________')
    clusterer.fit_predict(matrix_newcomer, y=None)
    print('_____________________________________')
    #
    af = AffinityPropagation().fit(matrix_newcomer)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    print(labels)
    n_clusters_ = len(cluster_centers_indices)

    print('Estimated number of clusters: %d' % n_clusters_)
    # print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
    # print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
    # print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
    # print("Adjusted Rand Index: %0.3f"% metrics.adjusted_rand_score(labels_true, labels))
    # print("Adjusted Mutual Information: %0.3f"% metrics.adjusted_mutual_info_score(labels_true, labels))
    # print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels, metric='sqeuclidean'))


    print(pyjokes.get_joke())


    from itertools import cycle

    plt.close('all')
    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        class_members = labels == k
        cluster_center = X[cluster_centers_indices[k]]
        plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
        for x in X[class_members]:
            plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.savefig('gre')

