while True:
    try:
        s = input()
        temp = ''
        ans = ''
        for i in s:
            if i.isalpha():
                temp += i
        temp = sorted(temp, key = str.upper)
        index = 0
        for ch in s:
            if ch.isalpha():
                ans += temp[index]
                index += 1
            else:
                ans += ch
        print(ans)
    except:
        break