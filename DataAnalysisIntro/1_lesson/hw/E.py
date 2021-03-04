def build_char_counter(word):
    counter = dict()
    for letter in word:
        counter[letter] = counter.get(letter, 0) + 1
    return counter


size = int(input())
counter_to_words = dict()
for _ in range(size):
    new_word = input()
    counter = frozenset(build_char_counter(new_word).items())
    counter_to_words.setdefault(counter, []).append(new_word)

for counter in counter_to_words:
    print(*counter_to_words[counter])
