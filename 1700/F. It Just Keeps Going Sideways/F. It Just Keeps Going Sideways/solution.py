t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total, block_sum = 0, 0
    for i in range(n):
        total += arr[i] * (n-i-1)

    arr_sorted = arr.copy()
    arr_sorted.sort()
    
    for i in range(n):
        block_sum += arr_sorted[i] * (n-i-1)
    
    smaller_count = [0] * (n+1)
    
    count = 1
    for i in range(1, n):
        if arr_sorted[i] != arr_sorted[i-1]:
            smaller_count[arr_sorted[i]] = count
        
        count += 1
    
    minimum = arr[n-1]+1
    max_decrease, min_index = 0, n-1
    for i in range(n-1, -1, -1):
        if arr[i] < minimum:
            minimum = arr[i]
            min_index = i
            max_decrease = max(max_decrease, i-smaller_count[arr[i]])
            
    max_decrease = max(max_decrease, min_index)     

    
    print(total - block_sum + max_decrease)
