class Solution:
    def findPosition(self, N , M , K):
        # code here
        if N == 1:
            return 1
        result = M%N+K-1
        
        if result == N:
            return result
            
        return result%N
        
        
        
        
        
        

