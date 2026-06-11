t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = True
    
    for i in range(min(n-k, k)):
        if b[i] != a[i] and b[i] != -1:
            ans = False
            break
    if ans:
        # for non overlapping region
        for i in range(k, n-k):
            if b[i] != a[i] and b[i] != -1:
                ans = False
                break
    if ans:
        for i in range(max(k, n-k), n):
            if b[i] != a[i] and b[i] != -1:
                ans = False
                break
    if ans:
        present = [0] * (n+1)
        
        for i in range(n-k, k):
            present[a[i]] = 1
            
        # for overlapping region
        for i in range(n-k, k):
            if b[i] != -1 and present[b[i]] == 0:
                ans = False
                break
            
            if b[i] != -1:
                present[b[i]] = 0
                
    if ans:
        print("YES")
    else:
        print("NO")
            
    
    
        
    
