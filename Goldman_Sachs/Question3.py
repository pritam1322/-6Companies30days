
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
    
        # Brute Force :
        # space : O(NxN)  Time : O(1)
        
        """    
        def product(arr):
            p = 1
            for i in arr:
                p = p * i
            return p
         
        result = 0
        for i in range(n):
            for j in range(i+1,n+1):
                if product(a[i:j]) < k:
                    result += 1
                    
        
        return result
        """
        
        # Two Pointer approach   product for every iteration . if product is greater than k divide till 
        # it becomes less than k.
        
        result = 0
        p = 1
        j = 0
        for i in range(n):
            p = p * a[i]        
            
            
            while j < n and p >= k:
                p = p // a[j]
                j += 1
                
            result += i-j+1
        
        return result