one_points = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
two_points = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
three_points = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
four_points = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
five_points = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
eight_points = ['J', 'X', 'Ш', 'Э', 'Ю']
ten_points = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']



word = input()
word = word.upper()

number_of_points = 0
for i in range(len(word)):
    if word[i] in one_points:
        number_of_points += 1
    if word[i] in two_points:
        number_of_points += 2
    if word[i] in three_points:
        number_of_points += 3
    if word[i] in four_points:
        number_of_points += 4
    if word[i] in five_points:
        number_of_points += 5
    if word[i]in eight_points:
        number_of_points += 8
    if word[i] in ten_points:
        number_of_points += 10


print(number_of_points)