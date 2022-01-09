#User function Template for python3

class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        res = []
        
        for i in range(len(s)):
            ans = set()
            for j in range(n):
                if s[0:i+1] in contact[j][0:i+1]:
                    ans.add(contact[j])
            if len(ans) == 0:
                res.append(str(0))
            else:
                
                res.append(sorted(ans))
        return res
      
      
      
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends
