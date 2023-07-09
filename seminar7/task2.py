from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_fathest_orbit(list_of_orbits):
    max = 0
    s = None
    n = None
    for i in range(len(list_of_orbits)):
        if list_of_orbits[i][0] == list_of_orbits[i][1]:
            continue
        s = pi * list_of_orbits[i][0] * list_of_orbits[i][1]
        if max < s:
            max = s
            n = i
        s = None
    return list_of_orbits[n]


print(find_fathest_orbit(orbits))