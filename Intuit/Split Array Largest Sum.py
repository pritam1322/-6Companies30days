class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
      """
        n = len(nums)
        dp = [[float('inf') for _ in range(m+1)]for _ in range(n)]
        
        prefix = [0]*n
        prefix[0] = nums[0]
        
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
            
        for i in range(n):
            dp[i][1] = prefix[i]
        
        dp[0][0] = 0
        
        for i in range(n):
            for j in range(2,m+1):
                for k in range(0,i):
                    
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1],prefix[i]-prefix[k]))
                    
        return dp[-1][-1]
      
   """
        n = len(nums)
        lo,hi = max(nums),sum(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2 
            curr = 0
            split = 1
            
            for i in nums:
                curr += i
                
                if curr > mid:
                    curr = i
                    split += 1
                    
            if split <= m:
                hi = mid
            else:
                lo = mid + 1
                
        return lo
