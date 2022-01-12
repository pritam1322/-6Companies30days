#User function Template for python3
import sys
class Solution:
    def minDifference(self, arr, n):
        # code here
        s = sum(arr)
        dp = [[0 for _ in range(s+1)]for _ in range(n+1)]
        
        
        for i in range(n+1):
            dp[i][0] = 1
        
        for j in range(1,s+1):
            dp[0][j] = 0
        
        m = sys.maxsize
        
        for i in range(1,n+1):
            for j in range(1,s+1):
                 
                 
                if arr[i-1] <= j :
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else :
                    dp[i][j] = dp[i-1][j]
            
        
        
        
        for i in range((s//2)+1):
            if dp[n][i] == True:    
                m = min(m, s - 2 * i)
        return m       
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minDifference(arr, N)
        print(ans)

# } Driver Code Ends
