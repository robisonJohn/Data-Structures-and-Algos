/*
So we know Quick Sort works by picking some pivot number from an array, positioning every
other number in the array in sorted order with respect to the pivot (all smaller numbers
to the pivot's left; all bigger numbers to the pivot's right), and then repeating the same
two steps on both sides of the pivot until the entire array is sorted

General Process:
Pick a random number from the input array (i.e. the first number) and let that number
be the pivot. Iterate through the rest of the array using two pointers, one starting
at the left extremity of the array and progressively moving 
*/

function quickSort(array) {
    // this is the main method where we call the recursive function on the array initially
    quickSortHelper(array, 0, array.length - 1)
    // when the helper function finishes, we return the sorted array
    return array;
}

function quickSortHelper(array, startIdx, endIdx) {
    // this is the base case --> when the left pointer exceeds the right pointer, we return the array because this means
    // the array is fully sorted
    if (startIdx >= endIdx) return;
    // we initialize the pivot at the start index
    const pivotIdx = startIdx;
    // we let the left pointer begin at the start index + 1
    let leftIdx = startIdx + 1;
    // we let the right pointer begin at the end index
    let rightIdx = endIdx;
    // while the right pointer is greater than the left pointer
    while (rightIdx >= leftIdx) {
        // if the left value is greater than the pivot and the right value is less than the pivot
        if (array[leftIdx] > array[pivotIdx] && array[rightIdx] < array[pivotIdx]) {
            swap(leftIdx, rightIdx, array);
        } // if the value at the left index is less than the pivot value, incremement the left index by 1
        if (array[leftIdx] <= array[pivotIdx]) {
            leftIdx += 1;
        }
        // if the value at the right index is greater than the pivot value, decrement the right value
        if (array[rightIdx] >= array[pivotIdx]) {
            rightIdx -= 1;
        }

    }
    // then we swap the pivot index and the right index in the array
    swap(pivotIdx, rightIdx, array);
    // we then create a boolean, leftSubArrayIsSmaller, that checks whether the rightIdx minus the startIdx is
    // less than the endIdx minus the rightIdx --> this is saying whether the left array is smaller than the right array
    const leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1);
    // if the left array is smaller than the right array
    if (leftSubarrayIsSmaller) {
        // recursively call quickSortHelper on the array from the start index to one minus the right index
        quickSortHelper(array, startIdx, rightIdx - 1);
        // recursively call quickSortHelper on the array from the right index + 1 to the end index
        quickSortHelper(array, rightIdx + 1, endIdx);
    } else {
        // if the right array is smaller than the left array
        // recursively call the quickSortHelper on the array from the right index + 1 to the end index
        quickSortHelper(array, rightIdx + 1, endIdx);
        // recursively call the quickSortHelper on the array from the start index to the right index - 1
        quickSortHelper(array, startIdx, rightIdx - 1);
    }
}
// this is the swap function 
function swap(i, j, array) {
    let temp = array[j];
    array[j] = array[i];
    array[i] = temp;
}