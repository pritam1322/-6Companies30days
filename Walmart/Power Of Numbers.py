#User function Template for python3

class Solution:
    #Complete this function
    def power(self,x,y):
        #Your code here
        
        temp = 0
        if( y == 0):
            return 1
        temp = self.power(x, int(y / 2)) % 1000000007
        if (y % 2 == 0):
            return (temp * temp) % 1000000007;
        else:
            return (x * temp * temp) % 1000000007;
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
