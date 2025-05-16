import heapq

def optimal_merge_pattern_heap(files):
    heapq.heapify(files)

    total_cost = 0

    while len(files) > 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)

        merge_cost = first + second
        total_cost += merge_cost

        heapq.heappush(files, merge_cost)

    return total_cost

# **Algorithm** OptimalMergePattern(files)

# // Merges a list of files with given sizes in an optimal order to minimize total merge cost.
# // Uses a min-heap to efficiently select the two smallest files at each step.
# // Returns the total cost of all merge operations.

# {
#     // Initialize a min-heap from the list of file sizes
#     heap := files;  
#     BuildMinHeap(heap);  

#     total_cost := 0;  

#     while size(heap) > 1 do  
#     {  
#         // Extract the two smallest files
#         first := ExtractMin(heap);  
#         second := ExtractMin(heap);  

#         // Merge the two files and compute cost
#         merge_cost := first + second;  
#         total_cost := total_cost + merge_cost;  

#         // Insert the merged file back into the heap
#         Insert(heap, merge_cost);  
#     }  

#     return total_cost;  
# }


def optimal_merge_pattern(files):
    total_cost = 0

    while len(files) > 1:
        files.sort()

        first = files.pop(0)
        second = files.pop(0)

        merge_cost = first + second
        total_cost += merge_cost

        files.append(merge_cost)

    return total_cost


# 5  5  5  5
#  10    10 
#     20 

# = 40

# 5  5  5  5
#  10 
#  15
#  20
# = 45