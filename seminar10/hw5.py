def line_slice(string):
    if len(string) > 2:
        return string[:2] + string[-2:]
    else:
        return ''
    

print(line_slice(input()))