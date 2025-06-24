def partition(arr, low, high):
    pivot = arr[low]  # choose first element as pivot
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Place pivot in its correct position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1  # return the partition index


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example usage
L = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", L)
quick_sort(L, 0, len(L) - 1)
print("Sorted Array:", L)
