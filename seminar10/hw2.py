def front_x(words):
    words.sort()
    for i in range(len(words)):
        if len(words[i]) > 0:
            if words[i][0] == 'x':
                words.insert(0, words.pop(i))
    return words


