size = int(input())
counter_to_words = dict()
for _ in range(size):
    new_word = input()
    counter_to_words.setdefault(str(sorted(new_word)), []).append(new_word)

for counter in counter_to_words:
    print(*counter_to_words[counter])
