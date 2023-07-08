n = int(input())
m = int(input())


list_n = [input() for i in range(n)]
list_m = [input() for i in range(m)]


unique = set(list_m + list_n)
unique = list(unique)
unique.sort()
print(unique)
