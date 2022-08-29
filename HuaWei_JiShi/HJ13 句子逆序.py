while True:
    try:
        s = input()
        s = s.split()[::-1]
        for i in s:
            print(i, end=' ')
    except:
        break