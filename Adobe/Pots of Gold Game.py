class Solution:
    def maxCoins(self,arr, n):
        # Code here
        memo = [[-1 for _ in range(100)]for _ in range(100)]
        
        def solve(i,j,Sum):
            
            if j == i:
                memo[i][j] = arr[i]
                return arr[i]
            
            if i+1 == j:
                return max(arr[i],arr[j])
                
            if memo[i][j] != -1:
                return memo[i][j]
                
                
            memo[i][j] = max(Sum - solve(i+1,j,Sum - arr[i]),
                       Sum - solve(i,j-1,Sum- arr[j]))
            
            return memo[i][j]   
            
        return solve(0,n-1,sum(arr)) 
        

#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends
