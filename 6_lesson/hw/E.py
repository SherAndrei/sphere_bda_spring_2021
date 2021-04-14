# %%
from itertools import tee
from itertools import zip_longest

def chain_loop(args):
    for tuple in zip_longest(*args):
        for elem in tuple:
            yield elem


if __name__ == '__main__':
    a = range(5)
    b = range(10)
    c = range(3)
    print(list(chain_loop([a, b, c])))
    print([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9])

    print("===================")

    a = [None, None, None]
    b = [1] * 5
    print(list(chain_loop([a, b])))
    print([None, 1, None, 1, None, 1, 1, 1])

    print("===================")

    a = (i for i in range(10))
    b = a
    print(list(chain_loop([a, b])))
    print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    print("===================")

    a = (i for i in range(3))
    print(list(chain_loop(tee(a, 5))))
    print([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
# %%
