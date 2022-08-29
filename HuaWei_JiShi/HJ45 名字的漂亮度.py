while True:
    try:
        n = int(input())
        from collections import Counter

        for i in range(n):
            l = input()
            c = Counter(l)
            value = 26
            ans = 0
            for num in sorted(c.values())[::-1]:
                ans += num * value
                value -= 1
            print(ans)
    except:
        break

