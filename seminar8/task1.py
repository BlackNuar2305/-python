def data_input():
    with open('file.txt', 'a', encoding='utf-8') as f:
        f.write(input('Введите данные пользователя: '))
        f.write('\n')

def Output_of_all_data():
    with open('file.txt', 'r') as f:
        print(f.read())

def data_search():
    with open('file.txt', 'r+') as f:
        list_1 = list(f.read().lower().split('\n'))
        data = input('Введите данные для поиска: ')
        for i in range(len(list_1)):
            list_1[i] = list_1[i].split()
        for i in range(len(list_1)):
            if data.lower() in list_1[i]:
                print(list_1[i])

def To_change_the_data():
    with open('file.txt', 'r+') as f:
        old_data = f.read().lower()
    data = input('Введите данные для изменения: ').lower()
    data1 = input("Введите новые данные: ")
    new_data = old_data.replace(data, data1)
    with open('file.txt', 'w') as f:
        f.write(new_data)
while True:
    act = int(input('Выберите действие. 1 - ввод данных, 2 - вывод данных,\n 3 - поиск данных, 4 - изменить или удалить данные, 0 - выход '))
    if act == 0:
        break
    elif act == 1:
        data_input()
    elif act == 2:
        Output_of_all_data()
    elif act == 3:
        data_search()
    elif act == 4:
        To_change_the_data()