import os

from clustering import partially_cluster
from querytest import get_data

features = ['extension', 'fileName', 'timeDiff', 'isCommitterAuthor', 'commitTime']


def list_to_matrix(data):
    matrix = []
    for dictionary in data:
        feature_list = []
        for name in features:
            feature_list.append(int(dictionary[name]))
        matrix.append(feature_list)
    return matrix


def stream_data():
    page = 2000
    amount = 1000
    data = get_data(page, amount)
    cl = None
    while data is not []:
        message = ""
        for commit in data:
            if message != commit["commitMessage"] and commit["commitMessage"] != "":
                extension = str(commit["extension"])
                index = extension.rfind('.')
                if index > -1:
                    extension = extension[index+1::]
                if extension.find("/") == -1 and extension.find("aux") == -1:
                    path = "messages/" + str(extension) + ".txt"
                    file = open(path, 'a')
                    try:
                        file.write(commit["commitMessage"]+"\n")
                    except UnicodeEncodeError:
                        pass
                    file.close()
                    message = commit["commitMessage"]
        page += 1
        data = get_data(page, amount)


if __name__ == "__main__":
    stream_data()