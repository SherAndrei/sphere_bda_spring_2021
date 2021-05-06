import sys


def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)


def get_numbers(left, right):
    sizeof_nums = 10
    length = right - left
    if length > sizeof_nums:
        return [left + i * length // sizeof_nums for i in range(sizeof_nums)] + [right]
    else:
        return [left + i for i in range(length + 1)]


def get_new_range(numbers):
    for i in range(1, len(numbers) - 1):
        print("?", numbers[i])
    print("+")
    answers = [bool(int(safe_input())) for i in range(len(numbers) - 2)]
    for i in range(len(answers)):
        if answers[i] is True:
            return (numbers[i], numbers[i + 1])
    return (numbers[-2], numbers[-1])


def find(left, right):
    sys.stdout.flush()
    range = get_new_range(get_numbers(left, right))
    if range[0] + 1 == range[1]:
        print("!", range[0])
        return
    find(*range)


find(1, 100001)
