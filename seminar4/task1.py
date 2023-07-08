my_list = []
string = input()


for i in range(len(string)):
    my_list.append(string[i])


n = 0
for i in range(len(my_list)):
    k = my_list[i]

    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            n = n + 1
            my_list[j] = f'{k}_{n}'
    n = 0

print(my_list)