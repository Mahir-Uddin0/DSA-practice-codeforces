t = int(input())

while t:
    n = int(input())
    tasks = []
    
    for _ in range(n):
        c, p = map(int, input().split())
        tasks.append((c, p))
        
    dp = 0
    
    for c, p in reversed(tasks):
        factor = 1 - p / 100
        dp = max(dp, c + factor * dp)
        
    print("{:.10f}".format(dp))
    
    t -= 1
