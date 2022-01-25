class Solution:
    def isWordExist(self, grid, word):
        #Code here
        
        n = len(grid)
        m = len(grid[0])
        
        def dfs(i,j,pos):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            if pos == len(word):
                return True
            if word[pos] == board[i][j]:
                temp = board[i][j]
                board[i][j] = '#'
                a = dfs(i+1,j,pos+1)
                b = dfs(i-1,j,pos+1)
                c = dfs(i,j+1,pos+1)
                d = dfs(i,j-1,pos+1)
                board[i][j] = temp
            
                return a | b | c | d
            else:
                return False
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False    
        
        
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n, m = map(int, input().split())
        board = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            board.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(board, word)
        if(ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends
