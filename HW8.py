'''
Задача №49 - с семинара:
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные;
2. Программа должна сохранять данные в текстовом файле;
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например, имя или фамилию
человека);
4. Использование функций. Ваша программа не должна быть линейной.

Домашнее задание:
Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, 
которую необходимо перенести из одного файла в другой.
Формат сдачи: ссылка на пулл в свой репозиторий.
'''

from os.path import exists
from csv import DictReader, DictWriter

def get_info():
    first_name = "Иван"
    last_name = "Иванов"
    phone_number = "89999887766"
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()

def create_file_copies(file_name_copies):
    with open(file_name_copies, 'w', encoding='utf-8') as data:
        data.write()

def get_copy_line():
    line_index = int(input("Введите номер строки для копирования: ")) - 1
    return line_index

def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'
file_name_copies = 'copies.csv'

def copy_file_line(file_name, file_name_copies, line_index):
    res_line = []
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = data.read()
        res = list(f_reader.split("\n"))
        if line_index < len(res):
            res_line.append(res[line_index])
        else:
            print('Такой строки в файле нет!\n')

    with open(file_name_copies, 'a', encoding='utf-8') as data_1:
        data_1.seek(2)
        data_1.write("\n")
        data_1.writelines("\n".join(res_line))

    if line_index < len(res):
        print(f'Строка № {line_index + 1} скопирована.\n')

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует. Создайте его")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            copy_file_line(file_name, file_name_copies, get_copy_line())

main()