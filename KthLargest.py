import heapq

def kth_lar(arr, k):
    heap = []
    for x in arr:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

arr = [1,3,2,4,5,8]
k = 4
print(kth_lar(arr, 7))