#User function Template for python3
class Solution:

    def matchPairs(self,nuts, bolts, n):
        # code here
        ele = [0]*9
        
        for i in range(n):
            if nuts[i] == '!':
                ele[0] = '!'
            elif nuts[i] == '#':
                ele[1] = '#'
            elif nuts[i] == '$':
                ele[2] = '$'
            elif nuts[i] == '%':
                ele[3] = '%'
            elif nuts[i] == '&':
                ele[4]= '&'
            elif nuts[i] == '*':
                ele[5] = '*'
            elif nuts[i] == '@':
                ele[6] = '@'
            elif nuts[i] == '^':
                ele[7] = '^'
            else:
                ele[8] = '~'
        
        
        
        j = 0
        
        for i in range(9):
            if ele[i] != 0 :
                nuts[j] = ele[i]
                bolts[j] = ele[i]
                
                j += 1
                
        
            
            
#{ 
#  Driver Code Starts




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
