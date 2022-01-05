#User function Template for python3
import collections
class Solution:
    def canPair(self, nuns, k):
        # Code here
        if n%2 != 0:
            return False
        d = collections.defaultdict(lambda:0)
        for i in range(n):
            d[((nuns[i]%k)+k)%k] += 1
        
        for i in range(n):
            
            rem = ((nuns[i]%k)+k)%k
            
            if 2*rem == k:
                if d[rem] % 2 != 0:
                    return False
            
            elif rem == 0:
                if d[rem] & 1:
                    return False
        
            elif d[rem] != d[k-rem]:
                return False
        return True
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if(ans):
            print("True")
        else:
            print("False")
# } Driver Code Ends