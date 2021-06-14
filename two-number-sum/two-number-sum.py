# Solution 1 runs in O(n^2) time | O(1) space
# This is the brute force appraoch which employs two for loops
'''
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []
'''

# Solution 2 runs in O(n) time | O(n) space
# Uses external space via a dictionary to check if the target sum minus
# a number already in the dictionary is equal to a remaining element
# within the list
'''
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []
'''

# Solution 3 runs in O(n(log(n))) time | O(1) space
# This solution initially sorts the array and then uses two pointers
# While sum < targetSum, move left pointer right
# While sum > targetSum, move right pointer left
# if left > right, we know the target objective is not in our list

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
