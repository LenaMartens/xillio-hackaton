import pickle

from sklearn.cluster import Birch


# Cluster the data for network training
def cluster(feature_matrix):
    brc = Birch(branching_factor=50, n_clusters=None, threshold=0.5, compute_labels=True)
    # Train cluster
    brc.fit(feature_matrix)
    # Save cluster for future use
    pickle.dumps(brc, open("cluster.p", "wb"))
    # return labels for samples
    return brc.predict(feature_matrix)


# Partition the corpus based on the cluster labels. A network will be trained on each partition
def partition_message_set(messages, clusters):
    partitions = {}
    for index, label in enumerate(clusters):
        if label in partitions:
            partitions[label].append(messages[index])
        else:
            partitions[label] = [messages[index]]
    return partitions

