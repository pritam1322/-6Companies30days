class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        n = len(piles)
        
        dp = [[-1 for _ in range(501)]for _ in range(501)]
        
        def solve(i,j,Sum):
            
            if i == j :
                dp[i][j] = piles[i]
                return piles[i]
            
            if i+1 == j:
                return max(piles[i],piles[j])
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if i < j:
                
                dp[i][j] =  max(Sum - solve(i+1,j, Sum-piles[i]), Sum - solve(i,j-1, Sum-piles[j])) 
            
                return dp[i][j]
            
            
            
        ans = solve(0,n-1,sum(piles))
        #print(ans)
        if ans > sum(piles) - ans:
            return True
        else:
            False
