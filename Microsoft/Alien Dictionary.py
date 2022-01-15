#User function Template for python3
import collections
class Solution:
    def findOrder(self,words, N, K):
    # code here
        def topo(visit,v,adj):
            visit[ord(v)-97] = True
            for i in adj[v]:
                if visit[ord(i)-97] == False:
                    topo(visit,i,adj)
                    
                    
        adj = collections.defaultdict(list)
            
        for i in range(N-1):
            minDis = min(len(words[i]),len(words[i+1]))
            idx = -1
            for j in range(minDis):
                if words[i][j] == words[i+1][j]:
                    continue
                else:
                    idx=j
                    break
            if idx != -1 and idx != minDis:
                adj[words[i][idx]].append(words[i+1][idx])
                    
        visit = [False] * k
        stack = []
        for i in range(k):
            if visit[i] == False:
                topo(visit, chr(i+97), adj)
                    
        stack.reverse()
        stack = " ".join(stack)
            
        return stack
            
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
