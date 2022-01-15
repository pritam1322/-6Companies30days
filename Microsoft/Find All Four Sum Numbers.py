#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        arr.sort()
        ans = []
        for i in range(len(arr)-3):
            for j in range(i+1,len(arr)-2):
                low = j+1
                high = len(arr) - 1
                
                while low < high :
                    s = arr[i] + arr[j] + arr[low] + arr[high]
                    
                    if s < k:
                        low += 1
                    elif s > k:
                        high -= 1
                    else:
                        res = sorted([arr[i],arr[j],arr[low],arr[high]])
                        if res not in ans:
                            ans.append(res)
                        low += 1
                        high -= 1
                    
        return ans
                
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends
