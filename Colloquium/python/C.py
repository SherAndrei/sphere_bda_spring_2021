from heapq import merge


def merge_sort(array):
    array = list(array)
    i = 1
    while i < len(array):
        answer = []
        for j in range(0, len(array), 2 * i):
            answer.extend(merge(array[j:j+i], array[j+i:j+2*i]))
        array = answer
        yield answer
        i *= 2
    return
