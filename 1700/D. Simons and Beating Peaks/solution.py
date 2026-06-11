def find_ans(l, r):
    stack2 = [(l, r, 0)]
    dp = {}
    
    while stack2:
        l, r, state = stack2.pop()
        
        if l >= r:
            dp[(l, r)] = 0
            continue
        
        if state == 0:
            stack2.append((l, r, 1))
            x = pos[query_mat[(l, r)]]
            stack2.append((x+1, r, 0))
            stack2.append((l, x-1, 0))
        else:
            x = pos[query_mat[(l, r)]]
            left_ans = dp[(l,x-1)]
            right_ans = dp[(x+1, r)]
            dp[(l, r)] = min(r-x+left_ans, x-l+right_ans)
    
    return dp[(l, r)]


t = int(input())

while t:
    n = int(input())
    arr = list(map(int, input().split()))
    
    pos = [0] * (n+1)
    range_pos = [[0, n-1] for _ in range(n+1)]
    stack = [arr[0]]
    pos[arr[0]] = 0

    for i in range(1, n):
        pos[arr[i]] = i
        
        if arr[i] < arr[i-1]:
            range_pos[arr[i]][0] = i
        else:
            while stack != []:
                if arr[i] > stack[-1]:
                    range_pos[stack[-1]][1] = i-1
                    stack.pop()
                else:
                    range_pos[arr[i]][0] = pos[stack[-1]] + 1
                    break
        
        stack.append(arr[i])
        
    query_mat = dict()
    for i in range(1, n+1):
        query_mat[(range_pos[i][0], range_pos[i][1])] = i
    
    l, r, ans = 0, n-1, 0
    ans = find_ans(l, r)
    
    print(ans)
    
    t -= 1
