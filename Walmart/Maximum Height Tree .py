class Solution:
    def height(self, N):
        # code here
        
        if N == 1:
            return 1
        
        s = 0
        for i in range(1,N+1):
            s += i
            
            if s > N:
                s-= i
                return i-1
