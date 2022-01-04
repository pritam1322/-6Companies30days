import heapq
def max_10_number(arr):
    heap = []
    
    for num in arr:
        heapq.heappush(heap,num)
        if len(heap) > 10:
            heapq.heappop(heap)
            
    return heapq.heappop(heap)
