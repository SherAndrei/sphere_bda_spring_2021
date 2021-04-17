from collections import defaultdict


def smartdict_nan(key):
    return 10 * key


N = 10

# smartdict = {}
# for key in range(N):
#     val = defaultdict(lambda: smartdict_nan(key))
#     smartdict[key] = val

# assert k == 9
# assert smartdict[1]['a'] == 90

# key = 5
# assert smartdict[1]['b'] == 50

"""
 Ошибка заключается в том, что по умолчанию при первом
 вызове оператора [] срабатывает лямбда, которая ищет
 значение key в глобальном скоупе, и срабатывает для него.
 Чтобы исправить ошибку предлагается следующее решение:
"""

smartdict = {}
for key in range(N):
    val = defaultdict(lambda key=key: smartdict_nan(key))
    smartdict[key] = val


assert smartdict[0]['a'] == 0
assert smartdict[1]['b'] == 10

"""
 Таким образом мы дали лямбде значение в ее локальном скоупе.
 Теперь она берет ожидаемое значение.
"""
