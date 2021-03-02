start_size = int(input())
str_numbers = input().split()
my_set = set()
for str_number in str_numbers:
    new_number = int(str_number)
    if new_number not in my_set:
        print(new_number, end=" ")
    my_set.add(new_number)
print()
print(start_size - len(my_set))