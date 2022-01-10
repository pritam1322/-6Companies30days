#User function Template for python3
import sys
class Solution:
    def matrixChainOrder(self, p, n):
        # code here
        
        st = ''
    
        
        def printpattern(i,j,dp,st):
            
            if i == j:
                st += char(65+j)
                return
            
            st += '('
            printpattern(i,dp[i][j]-1,dp,st)
            printpattern(dp[i][j],j,dp,st)
            st += ')'
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(1,n):
            dp[i][i] = 0
            
        for L in range(2,n):
            for i in range(1,n-L+1):
                j = i+L-1
                dp[i][j] = sys.maxsize
                
                for k in range(i,j):
                    cost =  dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                    
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                       
        
                    
        
        st = ""
        printpattern(1,n-1,dp,st)
        return st
                    
                        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = input().split()
        for i in range(n):
            p[i] = int(p[i])
        
        ob = Solution()
        print(ob.matrixChainOrder(p, n))
# } Driver Code Ends
