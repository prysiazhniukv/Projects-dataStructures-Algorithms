def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallet = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        small = findSmallest(arr)
        new_arr.append(arr.pop(small))
    return new_arr

print(selectionSort([3,4,1,5,6,8,9]))

    