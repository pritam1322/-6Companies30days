#User function Template for python3
class Solution:
    def numOfWays(self, n, x):
        # code here
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        maxLimit =int(pow(n,1.0/x))
    
        for i in range(2,maxLimit+1):
            cur = pow(i,x)
            
            for j in range(n,cur-1,-1):
                dp[j] += dp[j-cur]
                
        return dp[-1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n,x = input().split()
        n=int(n)
        x=int(x)
        ob = Solution();
        print(ob.numOfWays(n, x))

# } Driver Code Ends
