#User function Template for python3

class Solution:
    def max_of_subarrays(self,arr,n,k):
        '''
        you can use collections module here.
        :param a: given array
        :param n: size of array
        :param k: value of k
        :return: A list of required values 
        
        if cur ele is greater than elements in stack just pop() them and add cur ele to stack.
        if the sliding widow hits size == k then push top ele of stack in res.
        
        '''
        #code here
        
        i = 0 
        j = 0
        m = 0
        res = []
        stack = [0]
        
        while j < n:
            
            while len(stack)>0 and stack[-1] < arr[j]:
                stack.pop()
                
            stack.append(arr[j])
            
            
            if j-i+1 == k:
                res.append(stack[0])
               
                if stack[0] == arr[i]:
                    stack.pop(0)
                i += 1
               
                   
               
            j += 1
               
               
        return res
            


import atexit
import io
import sys
from collections import deque



def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends
