#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        
        if R == 0:
            return 1

        res = (N ** R//2) % 10000000007
        res = (res*res) % 10000000007
        
        if R % 2 == 0:
            return res
        else:
            return res * N
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
