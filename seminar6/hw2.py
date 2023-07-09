n = int(input())
my_list = [int(input()) for i in range(n)]
min = int(input())
max = int(input())
list_index = []

for i in range(n):
    if min < my_list[i] < max:
        list_index.append(i)
print(list_index)
