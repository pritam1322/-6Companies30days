#User function Template for python3


class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        
        """
        stack = []
        res = [0] * n
        stack.append(0)
        res[0] = 1
        
        for i in range(1,n):
            
            while len(stack) > 0 and a[stack[-1]] <= a[i]:
                stack.pop()
                
            if len(stack) > 0 :
                res[i] = i - stack[-1]
            else:
                res[i] = i + 1
                
            stack.append(i) 
            
        return res
            
      """
      # Without Stack
      
      
      res = [0] * n
        
        res[0] = 1
        
        for i in range(1,n):
            c = 1
            
            while (i-c)>=0 and a[i] >= a[i-c]:
                c += res[i-c]
                
            res[i] = c
            
        return res
        
        
                
                
        
        
        
        
        
        
    
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj = Solution()
        ans = obj.calculateSpan(a, n);
        print(*ans) # print space seperated elements of span array
# } Driver Code Ends
