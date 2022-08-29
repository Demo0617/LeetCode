while True:
    try:
        n = int(input())
        k1, k2, k3 = 1, 0, 0
        for i in range(n - 1):
            k3 += k2
            k2 = k1
            k1 = k3
        print(k3 + k2 + k1)
    except:
        break
