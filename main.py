from import_txt import imp_pb as imp_txt
from export_txt import exp_pb as exp_txt
from import_csv import imp_csv as imp_csv
from export_csv import exp_csv as exp_csv
import ui

# все методы импорта эскорта заносим в словарь чтобы не использовать if elif elif...
format_imp_dict = {'txt':imp_txt,'csv':imp_csv}
format_exp_dict = {'txt':exp_txt,'csv':exp_csv}

# Команды командной строки
# 1) Загрузить из (Формат: pb_import --format path/file.name)  formats = [txt, csv, json, xml]
# ???1.1) на будущее отлавливать если файла не существует (писать ошибку)???
# 2) Выгрузить из (Формат: pb_export --format path/file.name)  formats = [txt, csv, json, xml]
# Выходные данные из 1 и 2: data = (imp or exp, format, path)
# 3) Добавить новую запись (Формат: pb_add Фамилия Имя Телефон Описание )
# Выходные данные как: date = (add, (фамилия, имя, телефон, описание))
# 4) Удалить запись "по фамилии" (Формат: pb_remove Фамилия) - удаляется первое вхождение
# Выходные данные как: date (remove, фамилия)
# 5) Показать data в консоли (модуль принимает data, выдает print в консоли)
# 6) Команда exit - для прекращения работы приложения

# Данные справочника в системе выглядят как: pb_list = [[Фамилия, Имя, Телефон, Описание],[Фамилия, Имя, Телефон...], ...]
pb_list = []

# спрашиваем пользователя пока он не даст команду выйти
def start():
    resume_ = ask_user()
    while resume_:
        resume_ = ask_user()

# вызов нужного импорта
def make_import(format_type, path):
    return format_imp_dict[format_type](path)

# вызов нужного эксопрта
def make_export(format_type, path, data_list):
    return format_exp_dict[format_type](path, data_list)

# удаляет первое совпавшее вхождение
def remove_by_name(name): 
    global pb_list
    for e in pb_list:
        if e[0] == name:
            pb_list.remove(e)
            return True
    return False

# вызов опроса пользователя и обработка его ответа
def ask_user():
        global pb_list
        data = ui.what_operation()
        command = data[0]
        if command == 'import':
            format_type = data[1]
            path = data[2]
            pb_list = make_import(format_type,path)
            ui.print_msg(f'Импротирование выполнено')
            ui.print_msg(pb_list) #debugg code
            return True
        elif command == 'export':
            format_type = data[1]
            path = data[2]
            make_export(format_type, path, pb_list)
            ui.print_msg(f'Экспоритрование в файл {path} выполнено')
            return True
        elif command == 'add':
            new_line = data[1]
            pb_list.append(new_line)
            ui.print_msg(f'Запись {new_line} удачно добавлена в справочник')
            ui.print_msg(pb_list) #debugg code
            return True
        elif command == 'remove':
            name_to_search = data[1]
            if remove_by_name(name_to_search):
                ui.print_msg(f'Первая запись с фамилией "{name_to_search}" удалена из справочника')
            else:
                ui.print_msg(f'Удаление не произошло запись с фамилией "{name_to_search}" в справочнике отсутсвует')
            ui.print_msg(pb_list) #debugg code
            return True
        elif command == 'exit':
            return False

start()



