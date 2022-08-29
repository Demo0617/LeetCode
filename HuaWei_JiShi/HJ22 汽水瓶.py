num = int(input())
while num != 0:
    ans = num // 3
    empty = ans + (num % 3)
    while empty >= 3:
        ans += empty // 3
        empty = (empty % 3) + (empty // 3)
    if empty == 2:
        ans += 1
    print(ans)
    num = int(input())

