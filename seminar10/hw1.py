string_numbers = input()
list_numbers = []
try:
    for i in range(len(string_numbers)):
        list_numbers.append(int(string_numbers[i]))
except ValueError:
    print('That\'s not an int!')

print(sum(list_numbers))