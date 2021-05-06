def calculate_change(change):
    coins = {k: 0 for k in [10.0, 5.00, 2.00, 1.00, 0.50, 0.10, 0.05, 0.01]}
    for coin in coins:
        while (round(change - coin, 2)) >= 0:
            change -= coin
            coins[coin] += 1
    return coins


result = calculate_change(float(input()))
for coin in result:
    if result[coin] != 0:
        print("{:5.2f}\t{}".format(coin, result[coin]), sep="\n")
