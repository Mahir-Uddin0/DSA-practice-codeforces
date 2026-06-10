t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    grid = [set() for _ in range(n)]
    
    for i in range(n):
        num = arr[i]
        
        grid[i].add(num)
        
        if num == 1:
            grid[i].add(2)
            
        while num != 1:
            if num % 2 == 0:
                num = num //2
            else:
                num += 1
            grid[i].add(num)

    ans = 10**9 
    for target in grid[0]:
        found = True
        for i in range(n):
            if target not in grid[i]:
                found = False
                break
        
        if found:
            total_ops = 0
            for i in range(n):
                ops = 0
                num = arr[i]
                while num != target:
                    if num % 2 == 0:
                        num = num // 2
                    else:
                        num += 1
                    ops += 1 
                total_ops += ops
                
                   
            ans = min(ans, total_ops)
            
    print(ans)
            
        
