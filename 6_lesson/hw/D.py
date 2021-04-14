# %%
import functools

def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'ncalls'):
            wrapper.ncalls = 0
        wrapper.rdepth = 0
        res = func(*args, **kwargs)
        wrapper.ncalls += 1
        wrapper.rdepth += 1
        return res
    return wrapper


@counter
def func1():
    return


@counter
def func2(n, steps):
    if steps == 0:
        return

    func2(n + 1, steps - 1)
    func2(n - 1, steps - 1)


if __name__ == "__main__":
    func1()
    print(func1.ncalls, func1.rdepth)

    func1()
    print(func1.ncalls, func1.rdepth)

    func2(0, 5)
    print(func2.ncalls, func2.rdepth)

    func2(0, 3)
    print(func2.ncalls, func2.rdepth)
# %%
