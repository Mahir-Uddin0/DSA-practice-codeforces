t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = []
    sort_arr = []
    
    for i in range(n):
        a, b = map(int, input().split())
        sort_arr.append([a+b, i])
        arr.append([a,b])
        
    sort_arr.sort()

    result = []
    
    for lis in sort_arr:
        idx = lis[1]
        result.extend(arr[idx])
        
    print(*result)
