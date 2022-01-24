class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        TC - O(N*N)
        
        
        mn = min(piles)
        mx = max(piles)
        
        if len(piles) == 1:
            return 2
        
        ans = float('inf')
        
        for k in range(mn, mx+1):
            time = 0
            for i in piles:
                cur = math.ceil(i / k)
                time += cur
            if time <= h:
                ans = min(ans, k)
                
        return ans
        
        """
        # TC - O(nlogm)
        
        mn = 1
        mx = max(piles)
        
        
        
        
        
        while mn < mx:
            mid = (mx +mn) // 2
            time = 0
            for i in piles:
                cur = math.ceil(i / mid)
                time += cur
            if time <= h:
                mx = mid
                
            else:
                mn = mid + 1
                
                
                
                
            
        return mx
