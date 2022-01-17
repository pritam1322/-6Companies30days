# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        if sum(arr) % 2 != 0:
            return 0
        
        s1 = sum(arr) // 2
        dp = [[0 for _ in range(s1+1)] for _ in range(N+1)]
        
        
        for i in range(N+1):
            dp[i][0] = 1
            
        for j in range(1,s1+1):
            dp[0][j] = 0
        
        for i in range(1,N+1):
            for j in range(1,s1+1):
                
                if j >= arr[i-1]:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
        
#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends
