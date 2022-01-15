#User function Template for python3


class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        #Your code here
        mp = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        
        def dfs(i,cur,result):
            
            if i == N:
                result.append("".join(cur))
                return
            for j in mp[a[i]]:
                cur.append(j)
                dfs(i+1,cur,result)
                cur.pop()
        result = []
        dfs(0,[],result)
        return result
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
