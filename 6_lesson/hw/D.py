import functools


def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper.current_depth == 0:
            wrapper.ncalls, wrapper.rdepth = 0, 0

        wrapper.current_depth += 1
        wrapper.ncalls += 1

        res = func(*args, **kwargs)

        wrapper.rdepth = max(wrapper.rdepth, wrapper.current_depth)
        wrapper.current_depth -= 1
        return res

    wrapper.current_depth = 0
    return wrapper
