#User function Template for python3

class Solution:
    def kvowelwords(self, N,K):
        # code here
        """
        Apply permutation to fill spaces with 21 consonats and 5 vowels.
        
        """
        
        dp = [[0 for _ in range(K+1)]for _ in range(N+1)]
        
        mod = 1e9 + 7
        
        for i in range(N+1):
            for j in range(K+1):
                
                if i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][K] * 21) % mod
                    
                    if j > 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-1] * 5 % mod) % mod

        return int(dp[-1][-1])                        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N,K = map(int,input().split())
        ob = Solution()
        ans = ob.kvowelwords(N,K)
        print(ans)
# } Driver Code Ends
