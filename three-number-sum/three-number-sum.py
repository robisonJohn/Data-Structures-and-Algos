# Solution runs in O(n^2) time | O(n) space

'''
First, we sort the array.
We then initialize an empty array called triplets.
We then iterate through our original array from to len(array) - 2
    Because we are looking for a triplet, it doesn't make sense for us to proceed all the way to the end
    Within this for loop, we initialize a left pointer and a right pointer
    While the left pointer < right pointer:
        let the currentSum equal array[i] + array[left] + array[right]
        if currentSum is equal to the targetSum
            append array[i], array[left], and array[right] to the triplets array
            increment left
            decerement right
        else if currentSum is less than targetSum
            increment left pointer by one
        else if currentSum is greater than targetSum
            increment right pointer by one
return the array of triplets

'''

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets