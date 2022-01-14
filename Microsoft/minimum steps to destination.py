class Solution:
    def minSteps(self, D):
        # code here
        s = 0
        i = 0
        while s < D or (s-D)%2 != 0:
            i += 1
            s += i
        return i
            
