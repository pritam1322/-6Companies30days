#User function Template for python3

class Solution:
    def nextPalin(self,N):
        #code here
        
        def reverse(num,i,j):
            while (i < j) :
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
                i = i + 1
                j = j - 1
        
        
        N = list(N)
        n = len(N)
        
        if n <= 3:
            return -1
        
        mid = (n // 2) - 1
        i = mid - 1
        
        while i >= 0:
            if N[i] < N[i+1]:
                break
            i -= 1
            
        if i < 0:
            return -1
            
        smallest = i + 1
        j = i + 2
        
        while j <= mid:
            if N[j] > N[i] and N[j] < N[smallest]:
                smallest = j
            j += 1
        
        temp = N[i]
        N[i] = N[smallest]
        N[smallest] = temp
        
        
        temp = N[n-i-1]
        N[n-i-1] = N[n-smallest-1]
        N[n-smallest-1] = temp
        
        reverse(N,i+1,mid)
        
        if n%2 == 0:
            reverse(N,mid+1,n-i-2)
        else:
            reverse(N,mid+2,n-i-2)
            
            
        return "".join(N)
        
        
        
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.nextPalin(s))
# } Driver Code Ends
