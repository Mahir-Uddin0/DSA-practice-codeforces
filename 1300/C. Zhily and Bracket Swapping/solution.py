t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    
    a_balance, b_balance, valid = 0, 0, True
    
    for i in range(n):
        if a[i] == '(':
            a_balance += 1
        else:
            a_balance -= 1
            
        if b[i] == '(':
            b_balance += 1
        else:
            b_balance -= 1
        
        if a_balance < 0:
            a_balance += 2
            b_balance -= 2
            if b_balance < 0:
                valid = False
                break
        elif b_balance < 0:
            b_balance += 2
            a_balance -= 2
            if a_balance < 0:
                valid = False
                break
            
    if valid:
        if a_balance == 0 and b_balance == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
            
    
                
                
                
                
                
                
                
                
                
                
            
