def build_char_counter(word):
    counter = dict()
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter


size = int(input())
counter_to_words = dict()
for i in range(size):
    new_word = input()
    counter = frozenset(build_char_counter(new_word).items())
    if counter not in counter_to_words:
        counter_to_words[counter] = list()
    counter_to_words[counter].append(new_word)

for counter in counter_to_words:
    print(' '.join(counter_to_words[counter]))
