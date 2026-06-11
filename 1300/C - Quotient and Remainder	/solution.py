t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    
    q.sort(reverse = True)
    r.sort()
    
    count = 0
    
    q_idx, r_idx = 0, 0
    
    while True:
        y = r[r_idx] + 1
        x = y * q[q_idx] + r[r_idx]
        
        if x <= k:
            count += 1
            r_idx += 1
        
        q_idx += 1
        
        if q_idx >= n or r_idx >= n:
            break
    
    print(count)
