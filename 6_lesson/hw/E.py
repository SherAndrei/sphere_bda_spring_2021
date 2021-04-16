def chain_loop(args):
    is_finished = {iter(arg): False for arg in args}
    while False in is_finished.values():
        unfinished = filter(lambda elem: elem[1] is False, is_finished.items())
        for it, _ in unfinished:
            try:
                yield next(it)
            except StopIteration:
                is_finished[it] = True
