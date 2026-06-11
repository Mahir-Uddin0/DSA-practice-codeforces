t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    maximum = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] ^ arr[j] > maximum:
                maximum = arr[i] ^ arr[j]
                
    print(maximum)
    
