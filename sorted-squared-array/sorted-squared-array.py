# Solution 1 runs in O(nlongn) time | O(n) space - where n is the length of the input array

'''
In this first solution, we create an array of zeros that is the length of our input array
We then iterate through our original array and, for each element in the array, we square the value
and set this value equal to a corresponding value in the sorted squares array.
We then return the sorted array.
'''

'''
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()
    return sortedSquares
'''

# Solution 2 runs in O(n) time | O(n) space - where n is the length of the array
'''
Solution 2 gives us a more efficient time complexity because we no longer need to sort the 
given array. We still initialize an array of zeros and initialize two pointers at the smallest
and largest index, respectively.
We then iterate through the array in reverse order and let the smallerValue be equal to the value
of the array at the smaller index. Similarly, we let the largerValue be equal to the value of 
the array at the larger index.
We then compare the absolute values of each of these array values.
If the smallerValue is greater than the largerValue then we let the value in the new array equal
the value of the sorted squares array. Else, we set the sorted squares value equal to the larger 
index value. This way we will always insert the larger squared value into the array.
As we do this in reverse order, we will return a sorted array.

'''

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue 
            largerValueIdx -= 1
    return sortedSquares





