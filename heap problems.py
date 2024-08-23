####### HEAP PROBLEMS ###########
#Question 1:
# find the kth smallest element in an array:
def kthelement(arr,N,k):
    arr.sort()
    return arr[k-1]
    
arr = [12,3,5,7,19]
N = len(arr)
k = 2
result = kthelement(arr,N,k)
print("kth smallest element is:",result)

## finding kth smallest element using priority queue ##
import heapq
def kthsmallestelement(arr,N,k):
    # creating a max_heap priority queue
    max_heap = []   #his is a max heap (implemented as a min heap with negative values due to Python's heapq library storing elements in ascending order by default).

    for num in arr:
        heapq.heappush(max_heap,-num)  #This negative sign is used to simulate a max heap behavior with Python's min heap.
        if len(max_heap) > k:
            heapq.heappop(max_heap)
            
    return -max_heap[0]#After processing all elements, the root of max_heap (-max_heap[0]) will be the Kth smallest element in the original array arr. We return -max_heap[0] to get the actual smallest element.
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
K = 4
N = len(arr)
result = kthsmallestelement(arr,N,k)
print("kth smallest element is:",result)


####$$$$$ easy based problem ############
#----------------------------------------------------------------------------------------
##### finding the largest elemnent in an unsorted array #######

import heapq    #This line imports the heapq module, which provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.#it will create min heap by default

def kth_largest(arr,k):
    arr = [-elem for elem in arr]  #negate each eleemnt in array like [-3,-2,-1,-5,-6,-4]
    heapq.heapify(arr)             #min-heap[-6,-5,-4,-3,-2,-1]
    for i in range(k-1):    
        heapq.heappop(arr)       #pop the smallest(most negative element)k-1 times
    return -heapq.heappop(arr)    #return the negation of the number with(-)
    
arr = [3,2,1,5,6,4]  #1,2,3,4,5,6
k = 2
result = kth_largest(arr,k)
print("kth largest element is:",result)

#----------------------------------------------------------------------------------------

######## finding the kth smallest element in an array ###########
import heapq
def kth_smallest(arr,k):
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return heapq.heappop(arr)
    
arr = [22,7,4,1,9,10]
k = 2
result = kth_smallest(arr,k)
print("kth smallest element is:",result)



import heapq
def merge_k_sorted_list(lists):
    min_heap = []
    merged_list = []
    
    for i,list in enumerate(lists):
        if list:
            heapq.heappush(min_heap,(list[0],i,0))
            
    while min_heap:
        val,list_index,elem_index = heapq.heappop(min_heap)
        merged_list.append(val)
        if elem_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][elem_index+ 1],list_index,elem_index+1)
            heapq.heappush(min_heap,next_tuple)
    return merged_list
    
lists = [
    [1,4,5],
    [1,3,4],
    [2,6]
    ]
merged = merge_k_sorted_list(lists)
print("merge k sorted list is :",merged)


