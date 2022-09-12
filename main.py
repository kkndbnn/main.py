documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def people(doc_p, number_1):
    split = []
    for doc in doc_p:
        split.append(doc["number"])
    if number_1 in split:
        for document in doc_p:
            doc_number = document['number']
            if doc_number == number_1:
                return doc_number
    else:
        return 'Данного документу не существует'


def shelf(dir_2, number):
    split = []
    for dirs in dir_2.values():
        split += dirs
    if number in split:
        for k, v in dir_2.items():
            if number in v:
                return k

                break
    else:
        return 'Данного документу не существует'


def list(doc_s):
    for document in doc_s:
        return f'{document["type"]} "{document["number"]}" "{document["name"]}"'


def add(doc_a, dir_a, num_user, type_user, name_user, dire):
    if dire not in dir_a.keys():
        return 'Данной полки не существует'
    else:
        doc_a.append({"type": type_user, "number": num_user, "name": name_user})
        dir_a[dire].append(num_user)
        return doc_a[-1]


def command():
    while True:
        com = input('Введите комманду: ')
        if com == 'p':
            number_1 = input("Введите номер: ")
            people(documents, number_1)
            print(people(documents, number_1))
        elif com == 's':
            number = input('Введите номер: ')
            shelf(directories, number)
            print(shelf(directories, number))
        elif com == 'l':
            list(documents)
            print(list(documents))
        elif com == 'a':

            num_user = input('Введите номер документа: ')
            type_user = input('Введите тип документа: ')
            name_user = input('Введите имя: ')
            dire = input('Введите номер полки: ')
            add(documents, directories, num_user, type_user, name_user, dire)
        else:
            print('Такой команды не существует :(')
command()