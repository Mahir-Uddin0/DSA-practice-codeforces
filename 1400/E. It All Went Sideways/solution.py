t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total = 0
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i]:
            total += arr[i-1] - arr[i]
            arr[i-1] = arr[i]
    
    minimum = arr[n-1]
    min_index = n-1
    max_decrease = 0
    for i in range(n-1, -1, -1):
        if arr[i] < minimum:
            decrease = min_index - i - 1
            min_index = i
            minimum = arr[i]
            max_decrease = max(max_decrease, decrease)
            
    max_decrease = max(max_decrease, min_index)
            
    print(total+max_decrease)
