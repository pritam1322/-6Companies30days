#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here
        ans = 0
        if string[0] == '-':
            for i in range(1,len(string)):
                if ord(string[i]) >= ord('0') and ord(string[i]) <= ord('9'):
                
                    ans = ans * 10 + (ord(string[i]) - ord('0'))
                else:
                    return -1
        else:
            for i in range(len(string)):
                if ord(string[i]) >= ord('0') and ord(string[i]) <= ord('9'):
                
                    ans = ans * 10 + (ord(string[i]) - ord('0'))
                else:
                    return -1
        if string[0] == '-':
            return -ans
        else:
            return ans
          
          
          
          
          
          
          
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends
