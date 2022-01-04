def encode(arr):
    # Code here
    
    c = 1
    s = ""
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            c += 1
        else:
            s += arr[i] + str(c)
            c = 1
            
    s += arr[-1] + str(c)
    return s
    