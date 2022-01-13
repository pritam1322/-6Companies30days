#User function Template for python3



#Function to generate binary numbers from 1 to N using a queue.
def generate(N):
    # code here
    
    def d2b(num):
        binary = ""
        while num > 0:
            
            binary += str(num % 2)
            num = num // 2
        
        return binary[::-1]
    
    
    res = []
    
    for i in range(1,N+1):
        res.append(d2b(i))
        
    return res
    
    
    
    
    
    
    
    
    
    
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


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
        res = generate(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
# } Driver Code Ends
