
class Solution:
	def CountWays(self, str):
		# Code here
        
        
        n = len(str)
        dp = [0] * (n+1)
        dp[0] = 1 
        dp[1] = 1
        mod = 1000000007
        
        if n==1 and str[0] != '0':
            return 1
        if str[0] == '0':
            return 0
            
        for i in range(2,n+1):
            
        
            
            if str[i-1] > '0':
                dp[i] = dp[i-1]%mod
            
            if (str[i-2] == '1' or (str[i-2] == '2' and str[i-1] < '7')):
                dp[i] = (dp[i]%mod + dp[i-2]%mod)% (mod)
        
        
        return dp[n]
        
        
        
        
        

