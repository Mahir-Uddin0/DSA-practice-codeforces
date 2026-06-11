t = int(input())


for _ in range(t):
    n, x, y = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    minimum, min_index = n+1, 0
    for i in range(x, y):
        if arr[i] < minimum:
            minimum = arr[i]
            min_index = i
            
    # swap in the middle
    temp = arr[x : min_index]
    arr[x : x+y-min_index] = arr[min_index : y]
    arr[x+y-min_index : y] = temp
    
    # move left numbers
    end_left = 0
    for i in range(0, x):
        if arr[i] > minimum:
            break
        end_left = i+1
            
    if end_left == x:
        end_right = y
        for i in range(y, n):
            if arr[i] > minimum:
                break
            end_right = i+1
        
    # print the array
    #  left
    for i in range(0, end_left):
        print(arr[i], end=' ')
    if end_left == x:
        for i in range(y, end_right):
            print(arr[i], end=' ')
            
    # Middle
    for i in range(x,y):
        print(arr[i], end=' ')
        
    #  Right
    for i in range(end_left, x):
        print(arr[i], end=' ')
        
    if end_left == x:
        for i in range(end_right, n):
            print(arr[i], end=' ')
    else:
        for i in range(y, n):
            print(arr[i], end=' ')
        
    print()     
    
    
        

    
