#User function Template for python3

class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        queue = []
        freq = [0]*26
        ans = ''
        for i in range(len(A)):
            s = A[i]
            freq[ord(s)-97] += 1
            if freq[ord(s)-97] == 1:
                queue.append(s)
            else:
                while queue and freq[ord(queue[0])-97] > 1:
                    queue.pop(0)
            if queue:
                ans += queue[0]
            else:
                ans += "#"
            
            
        return ans
      
      
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)

# } Driver Code Ends
