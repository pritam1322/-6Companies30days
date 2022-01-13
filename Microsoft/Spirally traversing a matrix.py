#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        t = 0
        d = r-1
        lt = 0
        rt = c-1
        res = []
        level = 0
        
        while t <= d and lt <= rt:
            if level == 0:
                for i in range(lt,rt+1):
                    res.append(matrix[t][i])
                t += 1
            elif level == 1:
                for i in range(t,d+1):
                    res.append(matrix[i][rt])
                rt -= 1
                
            elif level == 2:
                for i in range(rt,lt-1,-1):
                    res.append(matrix[d][i])
                d -= 1
            elif level == 3:
                for i in range(d,t-1,-1):
                    res.append(matrix[i][lt])
                lt += 1
                
            level = (level + 1)%4
        return res
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
