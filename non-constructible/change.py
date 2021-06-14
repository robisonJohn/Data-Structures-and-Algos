# O(nlogn) time | O(1) space - where n is the number of coins
'''
First, we sort the array. 
Set a value called currentChangeCreated to zero initially.
For each coin in the coins array:
    if the value of this coin is greater than currentChangeCreated + 1, then we return currentChangeCreated + 1
    else, increment the currentChangeCreated by the value of the current coin
Return the currentChangeCreated + 1

Thus, we effectively keep a running count of each coin in the mix; and if at any point our coin value is greater than 
1 + currentSum, we know 1 + currentSum is the smallest value we cannot create
'''
def nonConstructibleChange(coins):
    coins.sort()

    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin
    return currentChangeCreated + 1