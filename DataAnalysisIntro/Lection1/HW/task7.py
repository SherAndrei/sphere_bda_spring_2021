import sys


def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)


def answer(number):
    print("!", number)


def ask(*args):
    for number in args:
        print("?", number)
    print("+")
    answer_from_user = list()
    for _ in args:
        answer_from_user.append(bool(int(safe_input())))
    return answer_from_user


def get_ranges(left, right):
    return left + (right - left) // 4, left + (right - left) // 2, left + 3 * (right - left) // 4


def find(left, right):
    sys.stdout.flush()
    if (left + 1 == right):
        answer(left)
        return
    ranges = get_ranges(left, right)
    (first, second, third) = ask(ranges[0], ranges[1], ranges[2])
    if first and second and third:
        find(left, ranges[0])
    elif second and third and not first:
        find(ranges[0], ranges[1])
    elif third and not second and not first:
        find(ranges[1], ranges[2])
    else:
        find(ranges[2], right)


find(1, 100000)
