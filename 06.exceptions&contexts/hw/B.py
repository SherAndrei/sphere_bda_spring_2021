from re import sub
from itertools import starmap
from operator import mul, mod, setitem, itemgetter
from functools import reduce


def solution1(arg):
    return list(map(lambda str: int(sub(r'\D', '', str[::-1])), arg))


def solution2(arg):
    return list(starmap(mul, arg))


def solution3(arg):
    return list(filter(lambda i: i % 6 in [0, 2, 5], arg))


def solution4(arg):
    return list(filter(None, arg))


def solution5(arg):
    return list(map(lambda x: setitem(x, "square", x["width"] * x["length"]), arg))


def solution6(arg):
    return list(map(lambda room: dict(**room, square=room['width']*room['length']), arg))


def solution7(arg):
    return reduce(set.intersection, arg)


def solution8(arg):
    return reduce(lambda D, new: setitem(D, new, D.get(new, 0) + 1) or D, arg, {})


def solution9(arg):
    return list(map(itemgetter('name'), filter(lambda s: s['gpa'] > 4.5, arg)))


def solution10(arg):
    return list(filter(lambda num: sum(map(int, num[::2])) == sum(map(int, num[1::2])), arg))


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
