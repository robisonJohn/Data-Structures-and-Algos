# Solution 1: O(n) time | O(1) space - where n is the length of the array

'''
The objective of this first solution is to determine whether the array breaks a designated direction.
First, we check if the length of the array is less than or equal to 2; if it is, then we know the array must be 
a monotonic array.
We can then designate the direction of the array to be the difference between the second element in the array from the 
first element. If the array is monotonic and direction is less than zero, we know the array must be either strictly decreasing.
Similary, if the array is monotonic and direction is greater than zero, we know the array must be strictly increasing.
Now that we have a direction, we can iterate through the remainder of the array from index 2 to the end of the array.
If the initial difference is 0, we reset difference to be the difference between the next two numbers.
We then continue on.
We then call a helper function, the breaksDirection function, that is a function of the following:
    1. direction value
    2. the array value at index i - 1
    3. the array value at index i
The breaksDirection function performs the following logic:
    Takes the difference between the array value at index i - 1 and the array value at index i
    if the direction value is less than zero, implies that:
        1. The array is strictly decreasing
        2. Therefore, array[i - 1] - array[i] must be greater than zero
    Thus, we can return difference < 0 
        1. If this is true, we know we have broken direction and the function will return false
        2. If this is false, the main function will continue running
    if the direction value is greater than zero, this implies:
        1. The array is strictly increasing
        2. array[i - 1] - array[i] must be less than zero
    Therefore, when we return difference > 0, if this evaluates to true, then we have failed our condition, 
    and the main function will return false.
    Else, we have satisifed our monotonic condition, and our main function will continue iterating throughout the array.
'''

def isMonotonic(array):
    if len(array) <= 2:
        return True
    
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i-1], array[i]):
            return False

    return True

def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0



# Solution 2: O(n) time | O(1) space

'''
Solution 2 represents much more concise logic. Here, we initialize two variables as representing the monotonicity of the function
Let isNonDecreasing represent the idea that the array is entirely non-decreasing
Let isNonIncreasing represent the idea that the array is enitrely non-increasing
We can then iterate through the length of the array
At each point in the array we can say the following:
    if the array at the current index is less than the array at the previous index
        Then the array is decreasing
        So we set isNonDecreasing = False, because the array is decreasing
    similarly, if the array at the current index is greater than the array at the previous index,
        Then the array is increasing
        So we set isNonIncreasing = False, because the array is increasing
At the end of this loop, we will have four possible cases:
isNonDecreasing  | isNonIncreasing
    T                   T               T   --> array is homogenous
    F                   T               T   --> array is monotonically decreasing
    T                   F               T   --> array is monotonically increasing
    F                   F               F   --> array is not monotonic
So we can see that our logical operators will always return us the correct solution.
# QED
'''

def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False
    
    return isNonDecreasing or isNonIncreasing