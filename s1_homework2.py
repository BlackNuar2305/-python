s = int(input())


if (s / 2) % 2 == 0:
    k = s / 2
    p = (s / 2) / 2
    se = (s / 2) / 2
else:
    k = s / 2 + 1
    p = (k / 2) / 2
    se = (k / 2) / 2


print(int(k, se, p))