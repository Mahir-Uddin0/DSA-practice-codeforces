t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total, count = 0, 0
    sum_set = set()
    sum_set.add(0)
    
    for i in range(n):
        total += arr[i]
        
        if total in sum_set:
            count += 1
            sum_set = set()
            
        sum_set.add(total)
            
    print(count)
