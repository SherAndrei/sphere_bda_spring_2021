def generate(n, counter_open=0, counter_close=0, ans=''):
    if counter_open + counter_close == 2 * n:
        yield ans
    if counter_open < n:
        yield from generate(n, counter_open + 1, counter_close, ans + '(')
    if counter_open > counter_close:
        yield from generate(n, counter_open, counter_close + 1, ans + ')')


def brackets(n):
    yield from generate(n, 0, 0, '')


if __name__ == '__main__':
    n = int(input())
    print(*brackets(n), sep='\n')
