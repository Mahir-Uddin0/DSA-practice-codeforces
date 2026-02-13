t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    b = b + b
    c = c + c
    
    first_multiple, sec_multiple = 0, 0
    
    for j in range(n):
        found = True
        for i in range(n):
            if b[j+i] > a[i]:
                continue
            else:
                found = False
                break
            
        if found:
            first_multiple += 1
            
    
    for j in range(n):
        found = True
        for i in range(n):
            if c[j+i] > b[i]:
                continue
            else:
                found = False
                break
            
        if found:
            sec_multiple += 1
            
    print(n * first_multiple * sec_multiple)
    
    t -= 1
