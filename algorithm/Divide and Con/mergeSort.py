# Merge function to merge two sorted arrays
def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    # Compare elements and merge into result
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Collect any remaining elements from left or right
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# Merge sort function
def merge_sort(L):
    if len(L) <= 1:
        return L

    # Find the middle point
    middle = len(L) // 2

    # Split into left and right halves
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])

    # Merge the sorted halves
    return merge(left, right)

# Example usage
L = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", L)
sorted_array = merge_sort(L)
print("Sorted Array:", sorted_array)




def merge(L, low, mid, high):
    result = []
    left_index = low
    right_index = mid + 1

    while left_index <= mid and right_index <= high:
        if L[left_index] < L[right_index]:
            result.append(L[left_index])
            left_index += 1
        else:
            result.append(L[right_index])
            right_index += 1

    while left_index <= mid:
        result.append(L[left_index])
        left_index += 1

    while right_index <= high:
        result.append(L[right_index])
        right_index += 1

    # Copy result back into original list
    for i in range(len(result)):
        L[low + i] = result[i]


def merge_sort(L, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(L, low, mid)
        merge_sort(L, mid + 1, high)
        merge(L, low, mid, high)

# Example usage
L = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", L)
merge_sort(L, 0, len(L) - 1)
print("Sorted Array:", L)
