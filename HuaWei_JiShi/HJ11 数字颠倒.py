while True:
    try:
        s = input()
        s = s[::-1]
        for i in s:
            print(int(i), end = '')
    except:
        break