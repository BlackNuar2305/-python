def number_of_donuts(string):
    try:
        string = int(string)
    except ValueError:
        return 'Тупица введи число'
    if string < 9 and string > 0:
        return f'Всего пончиков: {string}'
    elif string > 9:
        return f'Всего пончиков: много'
    else:
        return 'Количество пончиков не может быть отрицательным'
    

print(number_of_donuts(input()))
