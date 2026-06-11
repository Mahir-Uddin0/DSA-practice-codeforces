from math import gcd, lcm

t = int(input())

for _ in range(t):
    n, m, a, b = map(int, input().split())
    
    print()
    if gcd(n, a) == 1 and gcd(m, b) == 1 and gcd(n, m) <= 2:
        print("YES")
    else:
        print("NO")


