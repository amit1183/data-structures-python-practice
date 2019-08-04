
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        partition_position = partition(arr, low, high)
        quicksort(arr, low, partition_position-1)
        quicksort(arr, partition_position+1, high)


def call_quick_sort():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n-1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" %arr[i])


call_quick_sort()

