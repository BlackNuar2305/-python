def same_by(characteristic, objects):
    if len(objects) == 0:
        return 'same'
    for i in objects:
        if characteristic(i) == True:
            return 'different'
    return 'same'


values = [0,2,8,4]

print(same_by(lambda x: x % 2, values))