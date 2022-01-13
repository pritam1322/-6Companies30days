#User function Template for python3

class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        graph = [[] for _ in range(N)]
        
        for u,v in prerequisites:
            graph[v].append(u)
            
        def dfs(node):
            visit[node] = True
            res[node] = True
            
            
            for nei in graph[node]:
                if visit[nei] == False:
                    if dfs(nei) == True:
                        return True
                
                elif res[nei] == True:
                    return True
            res[node] = False
            return False
            
                
        
        visit = [False] * N
        res = [False] * N
        for i in range(N):
            if visit[i] == False:
                if dfs(i) == True:
                    return 0
        return 1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
