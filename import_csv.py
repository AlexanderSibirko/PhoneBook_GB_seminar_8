import csv


def imp_csv(path):
    with open(path) as f:
        data = []
        data = list(csv.reader(f, delimiter=";"))
    return data
