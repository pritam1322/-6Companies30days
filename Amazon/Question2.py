
"""
Time complexity : O(n), Space - O(1)

3 conditions 1) if arr[i-1] < arr[i] upper++ & i++
                2) if arr[i-1] > arr[i] lower++ & i++
                3) arr[i-1] == arr[i] i++
       ans = max(max, upper+lower+1)
"""

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        
        ans = 0
        i = 1
        
        while i<n:
            upper,lower = 0,0
            
            while i < n and arr[i-1] == arr[i]:
                i += 1
            
            while i < n and arr[i-1] < arr[i] :
                upper += 1
                i += 1
            while i < n and arr[i-1] > arr[i] :
                lower += 1
                i += 1
                
            if upper and lower:
                ans = max(ans, upper+lower+1)
                
        return ans
