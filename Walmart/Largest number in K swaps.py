class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        #code here
        # TLE generated !!!!!!!!!!
        
        def swap(string, i, j):
 
            return (string[:i] + string[j] +
                    string[i + 1:j] +
                    string[i] + string[j + 1:])
        
        def findMax(string,k,maxm):
            
            if k == 0:
                return
         
            n = len(string)
         
            
            for i in range(n - 1):
         
                
                for j in range(i + 1, n):
         
                    
                    if string[i] < string[j]:
         
                        
                        string = swap(string, i, j)
         
                        
                        if string > maxm[0]:
                            maxm[0] = string
         
                        
                        findMax(string, k - 1, maxm)
         
                        
                        string = swap(string, i, j)
                    
        maxm = [s]            
        findMax(s,k,maxm) 
        return maxm[0]
            
