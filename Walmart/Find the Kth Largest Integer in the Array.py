import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
        q = []
        heapq.heappush(q,int(nums[0]))
        
        for i in range(1,n):
            
            heapq.heappush(q,int(nums[i]))
            
            if len(q) > k:
                heapq.heappop(q)
                
            
        return str(q[0])
