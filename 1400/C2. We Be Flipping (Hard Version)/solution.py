t = int(input())

for it in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(n-1, -1, -1):
        if a[i] < 0:
            a.pop()
        else:
            break
     
    n, total_sum = len(a), 0
    
    if n == 0:
        print("0")
        print()
        continue
    
    for i in range(n):
        total_sum += a[i] if a[i] > 0 else -a[i]
    
    max_sum, max_index = sum(a), -1
    for i in range(n-1, -1, -1):
        if a[i] < 0:
            total_sum += 2*a[i]
        else:
            if total_sum - 2*a[i] > max_sum:
                max_sum = total_sum - 2*a[i]
                max_index = i
    
    even, result = True, []
        
    for i in range(max_index-1, -1, -1):
        if even:
            if a[i] > 0:
                result.append(i+1)
                even = False
            else:
                continue
        else:
            if a[i] < 0:
                result.append(i+1)
                even = True
            else:
                continue
    
    if max_index > 0:
        result.append(max_index+1)
    print(len(result))
    print(*result)
    
