t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse = True)
    
    odd = []
    even = []
    
    for i in range(n):
        if arr[i] % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
            
    odd_idx, even_idx = 0, 0
    
    result = [0] * n
    if odd:
        result[0] = odd[0]
      
    even_len, odd_len = len(even), len(odd)
    
    if odd_len == 0:
        print(*result)
        continue
    elif even_len == 0:
        result = [odd[0], 0] * (n // 2)
        if n % 2 == 1:
            result.append(odd[0])
        print(*result)
        continue
            
            
    for i in range(even_len):
        result[i+1] = result[i] + even[i]
        
    if odd_len == 2:
        result[-1] = 0
        print(*result)
        continue
    elif odd_len == 1:
        print(*result)
        continue
    
    first, sec = result[even_len-1], result[even_len]
    
    if odd_len % 2 == 0:
        result[even_len+1 : n-1] = [first, sec] * ((odd_len - 1) // 2)
    else:
        result[even_len+1 : ] = [first, sec] * ((odd_len - 1) // 2)
        

    print(*result)
        
