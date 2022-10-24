from math import sqrt
from pprint import pprint

from numpy.random import randint


def partition(lst):
    data = list(map(vector_into_strength, lst))
    data = sorted(data, reverse=True)
    teams = [[] for _ in range(15)]

    for iteration in range(15):
        for student_num in range(15):
            teams[student_num].append(data[iteration * 15 + student_num])
        teams = sorted(teams, key=vector_into_strength)

    return teams


def vector_into_strength(vector):
    """
    I use second norm to translate points of exam into strength
    :param vector:
    :return:
    """
    sum = 0
    for x in vector:
        sum += x ** 2
    return sqrt(sum)


arr = []
for _ in range(225):
    x = randint(0, 100)
    y = randint(0, 100)
    z = randint(0, 100)
    arr.append([x, y, z])
arr = partition(arr)

returned_val = sorted(list(map(vector_into_strength, arr)))

pprint(returned_val)
