#User function Template for python3

class Solution:
    
    #Function to count number of ways to reach the nth stair 
    #when order does not matter.
    
    def countWays(self,m):
        
        mod = 1000000007
        # code here
        return int((m/2)+1)% mod

      
      
      
      
      
      
      
import atexit
import io
import sys



if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends
