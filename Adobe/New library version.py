s1 = list(map(int,input().split(".")))
s2 = list(map(int,input().split(".")))


def solve(s1,s2):
    i = 0
    j = 0
    
    while i < len(s1) and j < len(s2):
        
        if s1[i] > s2[j]:
            return s1
            
        elif s1[i] < s2[j] :
            return s2
            
        i += 1 
        j += 1 

if solve(s1,s2) == s1:
    print("s1")
else:
    print("s2")
