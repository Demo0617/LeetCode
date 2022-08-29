while True:
    try:
        s = input()
        ans = [0, 0, 0, 0]
        for ch in s:
            if ch.isalpha():
                ans[0] += 1
            elif ch == ' ':
                ans[1] += 1
            elif ch.isdigit():
                ans[2] += 1
            else:
                ans[3] += 1
        for num in ans:
            print(num)
    except:
        break

