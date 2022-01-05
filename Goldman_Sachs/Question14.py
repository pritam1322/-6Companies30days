class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        s = 0
        min_len = n + 1
      
        
        while j < n:
            s += nums[j]
            
            if s >= target:
                
                while s >= target:
                    min_len = min(min_len,j-i+1)
                    s -= nums[i]
                    i += 1
                
                
                
            j += 1
            
        return min_len if min_len <= n else 0
            