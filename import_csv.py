import csv

def imp_csv(path):
    with open(path, encoding='UTF-8') as f:
        data = []
        data = list(csv.reader(f, delimiter=","))
    return data
