t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    a_count, b_count = 0, 0
    for i in range(n):
        if s[i] == 'a':
            a_count += 1
        else:
            b_count += 1
    
    if a_count == b_count:
        print("0")
        continue
    
    extra = a_count - b_count
    balance, ans = 0, n
    dic = {0 : -1}
    
    
    for i in range(n):
        if s[i] == 'a':
            balance += 1
        else:
            balance -= 1 
        
        dic[balance] = i
            
        if balance - extra in dic:
            ans = min(ans, i - dic[balance - extra])
            
    if ans == n:
        print("-1")
    else:
        print(ans)
