class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
        #code here
        
    
        
        if (L2[0] > R1[0] or R2[0] < L1[0]):
            return 0
        if (L2[1] < R1[1] or R2[1] > L1[1]):
            return 0
        
        return 1
            
        