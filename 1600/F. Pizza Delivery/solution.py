t = int(input())

while t:
    n, a_x, a_y, b_x, b_y = map(int, input().split())
    points = [[0, 0] for _ in range(n+2)]
    points[0] = [a_x, a_y]
    points[n+1] = [b_x, b_y]
    dp_top = [0] * (n+2)
    dp_down = [0] * (n+2)
    points_top = [[a_x, a_y]]
    points_down = [[a_x, a_y]]
    
    points_x = list(map(int, input().split()))
    points_y = list(map(int, input().split()))
    
    for i in range(n):
        points[i+1][0] = points_x[i]
        points[i+1][1] = points_y[i]
        
    points.sort()
    
    count = 0
    for i in range(1, n+2):
        if points[i][0] == points[i-1][0]:
            points_top[count] = points[i]
        else:
            count += 1
            points_top.append(points[i])
            points_down.append(points[i])
    
    
    for i in range(1, count + 1):
        x = points_top[i][0]-points_top[i-1][0]+points_top[i][1]-points_down[i][1]
        
        dp_top[i] = x  + min(dp_top[i-1] + abs(points_top[i-1][1] - points_down[i][1]), dp_down[i-1] + abs(points_down[i-1][1] - points_down[i][1]) )
        
        dp_down[i] = x + min(dp_top[i-1] + abs(points_top[i-1][1] - points_top[i][1]), dp_down[i-1] + abs(points_down[i-1][1] - points_top[i][1]) )
        
        
    print(min(dp_top[count], dp_down[count]))
        
    t -= 1
