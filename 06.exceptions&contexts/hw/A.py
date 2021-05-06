def solution1(arg):
    return [ch * 4 for ch in arg]


def solution2(arg):
    return [i * ch for i, ch in enumerate(arg, 1)]


def solution3(arg):
    return [el for el in arg if el % 3 == 0 or el % 5 == 0]


def solution4(arg):
    return [el for subarg in arg for el in subarg]


def solution5(arg):
    return [(i, j, k) for k in range(1, arg + 1)
            for j in range(1, k + 1)
            for i in range(1, j + 1)
            if i ** 2 + j ** 2 == k ** 2]


def solution6(arg):
    return [[x + shift for x in arg[1]] for shift in arg[0]]


def solution7(arg):
    return [[arg[j][i] for j in range(len(arg))]
            for i in range(len(arg[0]))]


def solution8(arg):
    return [list(map(int, str.split())) for str in arg]


def solution9(arg):
    return {chr(ord('a') + num): num ** 2 for num in arg}


def solution10(arg):
    return {name.lower().capitalize() for name in arg if len(name) > 3}


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
