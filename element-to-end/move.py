# O(n) time | O(1) space - where n is the length of the array
'''
The objective is to move all instances of a given integer to the end of the array
First, set two pointers, i and j
Set i equal to the first index of the array and j equal to the final index of the array
while i is less than j:
    while i is less than j and the element of array at index j is equal to the target value:
        decrement j by one
    if the value of array at index i is equal to the target value:
        swap the order of values positioned at index i and index j
    Increment index i by one
finally, return the value of the array
'''

def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array