string = [i for i in input().split()]
alf = ['а', 'у', 'о', 'ы', 'и', 'э', 'ю', 'ё', 'е', 'я']
n = len(string)

def col_phrase(s, a):
    col = 0
    for i in range(len(s)):
        if s[i].lower() in a:
            col += 1
    return col
count = col_phrase(string[1], alf)

for i in range(2, len(string)):
    if col_phrase(string[i], alf) == count:
        continue
    else:
        print('no')
        break
else:
    print('yes')
