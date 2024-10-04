def MinimumNumberOfCoins(coins, total):
    table = [float('inf')] * (total + 1)
    table[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                sub_result = table[i - coin]
                if sub_result != float('inf') and sub_result + 1 < table[i]:
                    table[i] = sub_result + 1
    return table[total]




def MaximumNumberOfCoins(coins, total):
    table = [float('-inf')] * (total + 1)
    table[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                table[i] = max(table[i], table[i - coin] + 1)
    return table[total]



def NumberOfWaysToMakeSum(coins, total):
    table = [0] * (total + 1)
    table[0] = 1
    for coin in coins:
        for i in range(coin, total + 1):
            table[i] += table[i - coin]
    return table[total]



print(NumberOfWaysToMakeSum([2,5,6,9],10))  
print(MinimumNumberOfCoins([2,5,6,9],10))
print(MaximumNumberOfCoins([2,5,6,9],10))