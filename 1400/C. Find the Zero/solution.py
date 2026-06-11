import sys
t = int(input())

for _ in range(t):
    n = int(input())
    ans = False
    
    for i in range(1, 2*n-2, 2):
        print(f'? {i} {i+1}')
        sys.stdout.flush()
        match = int(input())
        
        if match == 1:
            print(f'! {i}')
            ans = True
            break
        
    if not ans:
        print(f'? {2*n-3} {2*n-1}')
        sys.stdout.flush()
        match = int(input())
        
        if match == 1:
            print(f'! {2*n-3}')
        else:
            print(f'? {2*n-2} {2*n-1}')
            sys.stdout.flush()
            match = int(input())
            
            if match == 1:
                print(f'! {2*n-2}')
            else:
                print(f'! {2*n}')
            
        
    
    


    
     
