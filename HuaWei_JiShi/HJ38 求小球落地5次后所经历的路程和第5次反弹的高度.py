while True:
    try:
        h = float(input())
        total = h
        for i in range(4):
            total += h
            h = h / 2.0
        print(total)
        print(h / 2.0)


    except:
        break