import pickle

from sklearn.cluster import Birch


# Cluster the data for network training
def partially_cluster(cluster, feature_matrix):
    if cluster is None:
        cluster = Birch(branching_factor=50, n_clusters=None, threshold=0.5, compute_labels=True)
    # Partially add data to train cluster
    cluster.partial_fit(feature_matrix)
    # Save cluster for future use
    pickle.dumps(cluster, open("cluster.p", "wb"))
    # return cluster and all attributes, for further training and labeling
    return cluster


# Partition the corpus based on the cluster labels. A network will be trained on each partition
def partition_message_set(messages, clusters):
    partitions = {}
    for index, label in enumerate(clusters):
        if label in partitions:
            partitions[label].append(messages[index])
        else:
            partitions[label] = [messages[index]]
    return partitions

