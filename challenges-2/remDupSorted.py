import sys

def removeDuplicates(arr):
    if len(arr) < 2:
        return arr

    i = 0
    j = 1
    while j < len(arr):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
        j += 1

    i += 1
    while i < len(arr):
        arr[i] = 0
        i += 1

    return arr

arr = [2,3,5,5,7,11,11,11,11,13]
arr = [1,1,2,2,2]
print removeDuplicates(arr)
