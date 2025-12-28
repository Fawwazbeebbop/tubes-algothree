def greedy_recursive(change, coins, result=None):
    if result is None:
        result = {}

    if change == 0 or not coins:
        return result

    coin = coins[0]
    if change >= coin:
        result[coin] = result.get(coin, 0) + 1
        return greedy_recursive(change - coin, coins, result)
    else:
        return greedy_recursive(change, coins[1:], result)
