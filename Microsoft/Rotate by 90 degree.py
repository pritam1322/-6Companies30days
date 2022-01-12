#User function Template for python3

def rotate(matrix): 
    #code here
    n = len(matrix)
    
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    
    for i in range(n):
        for j in range(i+1):
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N=int(input())
        arr=[int(x) for x in input().split()]
        matrix=[]

        for i in range(0,N*N,N):
            matrix.append(arr[i:i+N])

        rotate(matrix)
        for i in range(N): 
            for j in range(N): 
                print(matrix[i][j], end =' ') 
            print() 
        

# } Driver Code Ends
