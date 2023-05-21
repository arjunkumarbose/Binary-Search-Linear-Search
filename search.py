def linear_search(arr, x):
    """
    Performs linear search to find the index of element x in the array arr.
    Returns -1 if x is not found in the array.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    """
    Performs binary search to find the index of element x in the sorted array arr.
    Returns -1 if x is not found in the array.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
