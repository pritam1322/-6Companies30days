#User function Template for python3

   
class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        #code here
     
        dp = [[0 for _ in range(b)]for _ in range(a)]
        
        for i in range(a):
            dp[i][0] = 1
        for i in range(b):
            dp[0][i] = 1
            
        for i in range(1,a):
            for j in range(1, b):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
                
                
        return dp[-1][-1]
    '''
        
        def dfs(r,c):
            
            nonlocal count
            
            if r == a and c == b:
                count += 1
                
            if r > a or c > b:
                return
            
            dfs(r+1, c)
            dfs(r,c+1)
            
            
        count = 0
        dfs(1,1)
        return count
   '''
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        ob = Solution()
        print(ob.NumberOfPaths(a, b))

# } Driver Code Ends
