import csv


def exp_csv(path, data):

    with open(path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
