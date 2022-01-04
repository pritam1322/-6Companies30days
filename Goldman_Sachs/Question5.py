class Solution:
	def getNthUglyNo(self,n):
		# code here
        
        
        ugly = [0] * n
        ugly[0] = 1
        
        
        i=0 
        j=0
        k=0
        
        i2=2; i3=3; i5=5
        
        for l in range(1,n):
            ugly[l] = min(i2,i3,i5)
            
            if ugly[l] == i2:
                i += 1
                i2 = ugly[i] * 2
            
            if ugly[l] == i3:
                j += 1
                i3 = ugly[j] * 3
                
            if ugly[l] == i5:
                k += 1
                i5 = ugly[k] * 5
            
        return ugly[n-1]