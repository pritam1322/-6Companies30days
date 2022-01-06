#User function Template for python3
# Time complexity = O(NxNxK)
class Solution:
    def maxProfit(self, K, N, A):
        # code here
        if N == 0:
            return 0
        
        dp = [[0 for i in range(N)]for j in range(K+1)]
        for i in range(1,K+1):
            for j in range(1,N):
                maxp = 0 
                for x in range(j,-1,-1):
                    maxp = max(maxp, dp[i-1][x] + (A[j]-A[x]))
                dp[i][j] = max(maxp, dp[i][j-1])
        
        return dp[-1][-1]
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends
