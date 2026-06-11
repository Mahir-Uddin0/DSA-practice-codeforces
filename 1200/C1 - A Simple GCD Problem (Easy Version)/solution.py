from math import gcd

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n == 2:
        g = gcd(a[0], a[1])
        ans = 0
        if g < a[0]:
            ans += 1
        if g < a[1]:
            ans += 1
        print(ans)
        continue

    g = []
    for i in range(n - 1):
        g.append(gcd(a[i], a[i + 1]))

    ans = 0

    if g[0] < a[0]:
        ans += 1

    for i in range(1, n - 1):
        l = g[i - 1] * g[i] // gcd(g[i - 1], g[i])
        if l < a[i]:
            ans += 1

    if g[-1] < a[-1]:
        ans += 1

    print(ans)
