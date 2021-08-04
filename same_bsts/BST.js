/*
An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer 
in the array, from left to right, into the BST.
Write a function that takes in two arrays of integers and determines whether these two arrays
represent the same BST. Note that you're not allowed to construct any BSTs in your code.
A BST is a Binary Tree that consists only of BST nodes. A node is said to be a valid BST node if and only if
it satisfies the BST property: its value is strictly greater than the values of every node to its left; its
value is less than or equal to the values of every node to its right; and its children nodes are either valid
BST nodes themselves or None / null.

i.e. consider 
arrayOne = [10,15,8,12,94,81,5,2,11]
arrayTwo = [10,8,5,15,2,12,11,94,81]
This would return true

#1 
You can immediately conclude that the input arrays don't represent the same BST if their first values 
aren't equal to each other, since their first values represent the root of the BST. 
Similarly, you can conclude this if their lengths are different.

#2
Given an array of integers, all of the values in the array that are smaller than the first value in the array
are located in the left subtree of the BST that the array represents, and all of the values in the array that
are greater than or equal to the first value in the array are located in the right subtree of the BST that the
array represents. 
Use this fact and #1 to recursively determine whether all subtrees in the BSTs represented by
the arrays are equal to each other.

#3
Write a recursive function that takes in two arrays of integers. 
If the first values of the arrays aren't equal to each other or if the arrays don't have the same length, 
then the arrays don't represent the same BST. 
If the first values and lengths are equal to each other, respectively, perform the following actions on 
both arrays:
    1. Gather all integers that are smaller than the first integer
    => Form an array with these integers representing the left subtree of the relevant BST
    2. Gather all integers that are greater than or equal to the first integer
    => Form an array with these integers representing the right subtree of the relevant BST
Call the recursive function twice: once with the two left-subtree arrays and once with the two right-subtree arrays

#4
Consider a solution where you don't need to create auxillary roles
*/

// O(n^2) | O(n^2) space - where n is the number of nodes in each array, respectively
    function sameBsts(arrayOne, arrayTwo) {
    // Write your code here.
        if (arrayOne.length !== arrayTwo.length) return false;
        
        if (arrayOne.length ===0 && arrayTwo.length === 0) return true;
        
        if (arrayOne[0] !== arrayTwo[0]) return false
        
        const leftOne = getSmaller(arrayOne);
        const leftTwo = getSmaller(arrayTwo);
        const rightOne = getBiggerOrEqual(arrayOne);
        const rightTwo = getBiggerOrEqual(arrayTwo);
        
        return sameBsts(leftOne, leftTwo) && sameBsts(rightOne, rightTwo)
    }
    
    function getSmaller(array) {
        const smaller = [];
        for (let i = 1; i < array.length; i++) {
            if (array[i] < array[0]) smaller.push(array[i]);
        }
        return smaller;
    }
    
    function getBiggerOrEqual(array) {
        const biggerOrEqual = []
        for (let i = 1; i < array.length; i++) {
            if (array[i] >= array[0]) biggerOrEqual.push(array[i]);
        }   
        return biggerOrEqual;
    }
    