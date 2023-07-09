list_1 = [int(i) for i in input().split()]
my_list = []
exp = lambda a: a * a

for i in list_1:
    if i % 2 == 0:
        my_list.append((i, exp(i)))

print(my_list)


def select(f, col):
    return [f(i) for i in col]


def where(f, col):
    return [i for i in col if f(i)]

data = [int(i) for i in input().split()]
res = select(int, data)
print
res = where(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)