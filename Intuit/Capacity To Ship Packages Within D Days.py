class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        lo = max(weights)
        hi = sum(weights)
        
        while lo < hi:
            
            mid = (lo+hi) // 2
            s = 0
            split = 1
            for x in weights:
                s += x
                
                if s > mid :
                    s = x
                    split += 1
                    
            if split <= days:
                hi = mid
            else:
                lo = mid + 1
            
        return hi
