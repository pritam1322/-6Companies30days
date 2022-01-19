#User function Template for python3
"""
Solution not working for many test cases!!!!!

"""

class Solution:
    def lengthOfLongestAP(self, A, n):
        # code here
        if n <= 2:
            return n
            
        dp = [[0 for _ in range(n)]for _ in range(n)]
        
        m = 2
        
        for i in range(n):
            dp[i][n-1] = 2
            
        for j in range(n-2,0,-1):
            
            i = j-1
            k = j+1
            
            while i >= 0 and k <= n-1:
                if A[i] + A[k] < 2 * A[j]:
                    k += 1
                elif A[i] + A[k] > 2 * A[j]:
                    dp[i][j] = 2
                    i -= 1
                else:
                    dp[i][j] = dp[j][k] + 1
                    
                    m = max(m,dp[i][j])
                    
                    i -= 1
                    k += 1
                    
                    while i >= 0:
                        dp[i][j] = 2
                        i -= 1
        return m
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.lengthOfLongestAP(A, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
