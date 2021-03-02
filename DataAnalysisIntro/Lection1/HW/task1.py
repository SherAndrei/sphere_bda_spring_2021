start_size = int(input())
my_set = set()
for number in [int(i) for i in input().split()]:
    if number not in my_set:
        print(number, end=" ")
    my_set.add(number)
print('', start_size - len(my_set), sep='\n')
