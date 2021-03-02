def calculate_change(change):
    coins = {
        10.0: 0,
        5.00: 0,
        2.00: 0,
        1.00: 0,
        0.50: 0,
        0.10: 0,
        0.05: 0,
        0.01: 0
    }
    for coin in coins:
        while (round(change - coin, 2)) >= 0:
            change -= coin
            coins[coin] += 1
    return coins


change = float(input())
result = calculate_change(change)
for coin in result:
    if result[coin] != 0:
        print("{:5.2f}\t{}".format(coin, result[coin]), sep="\n")
