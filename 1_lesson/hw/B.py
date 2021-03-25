def sum_of_digits(string_num):
    return (sum([int(char_digit) for char_digit in list(string_num)]), int(string_num))


start_size = int(input())
print(*sorted(input().split(), key=sum_of_digits))
