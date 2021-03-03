def counter_to_words():
    counter = dict()
    for word in [i.lower() for i in input().split()]:
        if word not in counter:
            counter[word] = 0
        counter[word] += 1
    return counter


def compare_counters(first, second):
    for word in second:
        if word not in first:
            return False
        if first[word] < second[word]:
            return False
    return True


print("YES" if compare_counters(counter_to_words(), counter_to_words()) else "NO")
