def imp_pb(path):
    data = []
    data_collection = []
    lines_list = [line.replace('\n','') for line in open(path,'r', encoding='UTF-8').readlines()]
    for line_ in lines_list:
        if line_:
            data_collection.append(line_)
        else:
            data.append(data_collection)
            data_collection = []
    return data

# debug codes !!!remove on prod
# path = 'pb.txt'
# print(imp_pb(path))