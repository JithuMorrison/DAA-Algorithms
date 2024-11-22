import math

def greedy_change(amount, denominations):
    denominations.sort(reverse=True)
    result = []
    for coin in denominations:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

def dp_change(amount, denominations):
    dp = [float('inf')] * (amount + 1)
    coin_used = [-1] * (amount + 1)
    dp[0] = 0
    for coin in denominations:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    if dp[amount] == float('inf'):
        return -1, []
    result = []
    while amount > 0:
        result.append(coin_used[amount])
        amount -= coin_used[amount]
    return dp[-1], result

amount=6
denominations = [1,3,4]

change = greedy_change(amount, denominations)
print("Denominations : ",denominations)
print("Change for", amount, ":", change)

min_coins,coins = dp_change(amount, denominations)
print("\nMinimum coins needed for", amount, ":", min_coins)
print("Coins used : ",coins)
