def exp(a, b):
    if b == 1:
        return a
    return a * exp(a, b - 1)

a = int(input())
b = int(input())

print(exp(a, b))