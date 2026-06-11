t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    sm, zero_idx = 0, -1
    for i in range(n):
        if arr[i] == 0:
            zero_idx = i
        else:
            sm += arr[i] - 1
    
    best = n - zero_idx - 1
        
    print(best - max(n-1-sm, 0))
    
