#User function Template for python3

class Solution:
    def util(self,pat,rem,op,n):
        res=[]
       
        if rem<0 or op>n:
            return res
           
        if rem==0 and op==n:
            res.append(pat)
            return res
       
        if op<=n:
            res=self.util(pat+'(',rem+1,op+1,n)
               
        if rem!=0:
            res+=self.util(pat+')',rem-1,op,n)
       
        return res
       
       
    def AllParenthesis(self,n):
        rem=1
        op=1
        pat='('
        return self.util(pat,rem,op,n)
    
                    
#{ 
#  Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends
