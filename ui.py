def what_operation():
    operation_set = ['import', 'export', 'add', 'remove']
    input_operation = input('Введите тип операции(import/export/add/remove): ')
    if input_operation == operation_set[0] or input_operation == operation_set[1]:
        format, path = input('txt/csv: '), input('path: ')
        return [input_operation, format, path]
    if input_operation == operation_set[2]:
        adding_data = [input_operation, [input('Фамилия: '), input('Имя: '), input('Телефон: '), input('Описание: ')]]
        return adding_data
    if input_operation == operation_set[3]:
        return [input_operation, input('Фамилия удаляемого: ')]
    
