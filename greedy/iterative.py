def greedy_iterative(change, coins):
    result = {}
    for coin in coins:
        count = change // coin
        if count > 0:
            result[coin] = count
            change -= coin * count
    return result