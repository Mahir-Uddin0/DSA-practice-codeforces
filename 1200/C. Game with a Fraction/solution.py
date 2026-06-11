t = int(input())


while t:
    p, q = map(int, input().split())
    
    difference = q - p
    
    first = difference * 2
    second = difference * 3
    
    if p-first == q-second and p-first>=0 and q-first>=0 and difference > 0:
        print("Bob")
    else:
        print("Alice")
    
    
    
    t -= 1
