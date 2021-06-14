# Solution 1 runs in O(n) | O(1) space, where n is the length of the array 
'''
the length of the array
set two pointers, arrIdx and seqIdx
while arrIdx < array length and seqIdx < sequence length:
    check if the values at these indices are equal
    if they are equal, iterate seqIdx by one
    if they are not equal, iterate arrIdx by one
    if the subsequence property is to be satisfied, then seqIdx must equal the length of the sequence
'''

'''
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)
'''

# Solution 2 runs in O(n) time | O(1) space
# Solution 2 just uses one pointer and a for loop
'''
First, we initialize the pointer at 0. Then we iterate through the array and say, for each value in the array, check 
two conditions: 
    1. is the pointer equal to the length of the sequence? if so, break
    2. is the value of the sequence at the pointer index equal to the value in the array? if so, iterate pointer by one
Thus, if each item in the sequence is contained in the array, it will return true when we compare seqIdx to the length of
the sequence.
'''

def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)