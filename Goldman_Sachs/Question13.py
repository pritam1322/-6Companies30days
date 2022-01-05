#User function Template for python3

class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        
        
        for i in range(len(s)):
            if s[i] == ']':
                temp = ""
                while stack[-1] != '[':
                    temp = stack[-1] + temp
                    stack.pop()
                    
                stack.pop()
                num = ""
            
            
                while len(stack) > 0 and stack[-1].isdigit():
                    num = stack[-1] + num
                    stack.pop()
                    
                num = int(num)
                
                
                temp = temp * num
                stack.append(temp)
            else:
                stack.append(s[i])
                
        return stack[0]
            
                
                
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends