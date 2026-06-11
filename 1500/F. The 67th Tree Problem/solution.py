t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    if x > y:
        print("NO")
        continue
    if x == 0:
        if y % 2 == 0:
            print("NO")
        else:
            print("YES")
            for i in range(2, y+1):
                print(f"1 {i}")
        
        continue
    
    
    print("YES")
    for i in range(1, 2*x):
        print(f"{i} {i+1}")
        
    for i in range(2*x+1, x+y+1):
        print(f"{2*x} {i}")
    
    
