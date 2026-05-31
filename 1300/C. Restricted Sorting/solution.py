t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    sorted_arr = sorted(arr)
    
    displaced = []
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            displaced.append(arr[i])
            

    size = len(displaced)

    if size == 0:
        print("-1")
        continue
    
    largest, smallest, k = sorted_arr[-1], sorted_arr[0], 10**9
    mid = (largest + smallest) // 2
    
    for i in range(size):
        if displaced[i] > mid:
            k = min(k, displaced[i] - smallest)
        elif displaced[i] < mid:
            k = min(k, largest - displaced[i])
        else:
            k = min(k, max(largest-mid, mid-smallest))
        
    print(k)
        
