def is_palindrom(arr, l, r):
    palindrom = True
    while r >= l:
        if arr[l] == arr[r]:
            l += 1
            r -= 1
        else:
            palindrom = False
            break
            
    return palindrom
        
def count_mex(arr):
    n = max(arr)
    present = [0] * (n+1)
    for i in range(len(arr)):
        present[arr[i]] = 1
    
    for i in range(n+1):
        if present[i] == 0:
            return i
    return n+1

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mex = 1
    
    l, r = -1, -1
    for i in range(2*n):
        if arr[i] == 0:
            if l == -1:
                l = i
            else:
                r = i
                break
            
    if is_palindrom(arr, l, r):
        while l > 0 and r < 2*n-1:
            if arr[l-1] == arr[r+1]:
                l -= 1
                r += 1
            else:
                break
        if l < r:
            mex = max(mex, count_mex(arr[l:r+1]))

    
    l, r = -1, -1
    for i in range(2*n):
        if arr[i] == 1:
            if l == -1:
                l = i
            else:
                r = i
                break
            
    if is_palindrom(arr, l, r):
        while l > 0 and r < 2*n-1:
            if arr[l-1] == arr[r+1]:
                l -= 1
                r += 1
            else:
                break
        if l < r:
            mex = max(mex, count_mex(arr[l:r+1]))

    print(mex)
    
