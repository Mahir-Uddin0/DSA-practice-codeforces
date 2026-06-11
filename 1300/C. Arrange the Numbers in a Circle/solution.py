t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if sum(arr) < 3:
        print(0)
        continue
    self_accomodate = 0
    one_count = 0
    groups = 0
    one_accomodate = 0
    single_big = 0

    for x in arr:
        if x > 1:
            groups += 1
            self_accomodate += x
            single_big = x
            one_accomodate += (x - 2) // 2
        else:
            one_count += 1

    if groups == 0:
        print(0)
    elif groups == 1:
        print(self_accomodate + min(one_count, single_big // 2))
    else:
        print(self_accomodate + min(one_count, one_accomodate))
