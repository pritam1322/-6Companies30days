#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        d = {}
        name = []
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]] = 1
            else:
                d[arr[i]] += 1
                
        m = max(d.values())
        
        for k,v in d.items():
            if v == m:
                name.append(k)
        
        return min(name), m
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends
