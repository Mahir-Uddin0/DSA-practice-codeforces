t = int(input())

for _ in range(t):
    n, x, s = map(int, input().split())
    guests = input()
    
    i_seat, a_hand, e_seat, ans = x, 0, 0, 0
    
    for j in range(n):
        if guests[j] == 'I':
            if i_seat:
                i_seat -= 1
                e_seat += s-1
                ans += 1
        elif guests[j] == 'E':
            if e_seat:
                e_seat -= 1
                ans += 1
            elif a_hand and i_seat:
                i_seat -= 1
                a_hand -= 1
                e_seat += s-1
                ans += 1
        elif guests[j] == 'A':
            if e_seat:
                e_seat -= 1
                ans += 1
                a_hand += 1
            elif i_seat:
                i_seat -= 1
                e_seat += s-1
                ans += 1
            else:
                break
            
    print(ans)        
