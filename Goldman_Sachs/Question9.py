class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        
        """
        If string is of len = 5 then result will contain 6 digits.
        if string starts with 3 I then largest number will be at 3 position in array/string.
        if string starts with 3 D then smallest number will be at 3 position in array/string and then increasing order.
        """
        ans = ""
        stack = []
        num = 1
        
        for i in S:
            if i == "D":
                stack.append(num)
                num += 1
            else:
                stack.append(num)
                num += 1
                
                while len(stack) > 0:
                    ans += str(stack.pop())
                    
        stack.append(num)
        while len(stack) > 0:
            ans += str(stack.pop())
        
        return ans      