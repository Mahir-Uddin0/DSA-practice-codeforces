t = int(input())

for _ in range(t):
    t, h, u = map(int, input().split())
    n = 0
    prev = None
    if t and u:
        mn = min(t, u)
        n += 4 * mn
        t -= mn
        u -= mn
        
    if t and h :
        if t <= 2 * h:
            n += 3 * h + 2 * t
            t -= t
            h -= h
    if t:
        n += 2 * t + 1
    if h:
        n += 3 * h
    if u:
        n += 3 * u
        
    print(n)
