import csv


def exp_csv(path, data):

    with open(path, "w", newline='', encoding='UTF-8') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerows(data)
