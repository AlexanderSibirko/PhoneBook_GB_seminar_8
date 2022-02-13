def exp_pb(path, data):
    file_ = open(path,'w', encoding='UTF-8')
    for line in data:
        for e in line:
            file_.write(str(e) + '\n')
        file_.write('\n')
    file_.close

# debugg codes !!!remove on prod
# path = 'pb.txt'
# exp_pb(path,[['Фамилия_1','Имя_1',555-55-55,'кино'],['Фамилия_2','Имя_2',555-55-54,'кино_2'],['Фамилия_2','Имя_2',555-55-54,'кино_2']])
