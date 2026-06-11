t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans, keep_minus_ans = 0, -10**15
    if arr[0] < 0:
        ans += 2 * arr[0]
        keep_minus_ans = sum(arr[1:]) * (-1) 
    
    for i in range(n):
        if arr[i] > 0:
            ans += arr[i]
        else:
            ans -= arr[i]
        
    i, mn = n-1, 10**15
    
    while arr[i] < 0 and i > 0:
        mn = min(mn, abs(arr[i]))
        i -= 1
    mn = min(mn, abs(arr[i]))
    
    print(max( ans - mn, keep_minus_ans))
