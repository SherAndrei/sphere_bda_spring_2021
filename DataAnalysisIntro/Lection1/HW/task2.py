def sum_of_digits(x):
    result = 0
    for digit in list(x):
        result += int(digit)
    return (result, int(x))


start_size = int(input())
print(' '.join(sorted(input().split(), key=sum_of_digits)))
