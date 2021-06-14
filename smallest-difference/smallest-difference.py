# O(nlog(n) + mlog(m)) time | O(1) space
'''
First, we sort both arrays
Then set two pointers equal to 0
let two numbers, smallest and current, equal infinity
Initialize an empty array called smallestPair
while both pointers are less than the length of their respective arrays:
    let a variable called firstNum equal the value of arrayOne at idxOne
    let a variable called secondNum equal the value of arrayTwo at idxTwo
    compare firstNum and secondNum -->
    if firstNum < secondNum:
        let current equal the difference between secondNum and firstNum
        iterate idxOne by one
    else if secondNum < firstNum:
        let current equal the difference between firstNum and secondNum
        iterate idxTwo by one

    else:
        return firstNum, secondNum
    
    Then, if the value for smallest is greater than the value for current:
        let smallest be equal to current
        let the smallestPair equal the pair firstNum, secondNum
    
    at the end, return the smallest pair


'''


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
