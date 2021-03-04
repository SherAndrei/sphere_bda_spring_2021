def counter_to_words(sentence):
    counter = dict()
    for word in sentence.split():
        counter[word.title()] = counter.get(word.title(), 0) + 1
    return counter


def compare_counters(first, second):
    for word in second:
        if word not in first or first[word] < second[word]:
            return False
    return True


print("YES" if compare_counters(counter_to_words(input()),
                                counter_to_words(input()))
      else "NO")
