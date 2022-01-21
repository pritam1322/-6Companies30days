#User function Template for python3
import sys
class Solution:
    def minDifference(self, arr, n):
        # code here
        s1 = sum(arr) 

            
        dp = [[0 for _ in range(s1+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1
            
            
        for i in range(1,n+1):
            for j in range(1,s1+1):
                if j >= arr[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        m = float('inf')
        for i in range((s1//2)+1):
            if dp[n][i] == True:
                m = min(m, s1 - 2 * i)
                
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
