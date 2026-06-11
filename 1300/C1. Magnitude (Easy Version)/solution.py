t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp_pos = [0] * (n+1)
    dp_neg = [0] * (n+1)
    
    for i in range(n):
        dp_pos[i+1] = max(abs(dp_pos[i] + arr[i]), abs(dp_neg[i] + arr[i]) )
        dp_neg[i+1] = min( dp_pos[i] + arr[i], dp_neg[i] + arr[i] )
        
    print(max(dp_pos[n], abs(dp_neg[n])))
        
