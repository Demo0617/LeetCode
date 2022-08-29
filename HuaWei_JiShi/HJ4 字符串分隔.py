while True:
    try:
        s = input()
        for i in range(0, len(s),8):
            print('{:0<8}'.format(s[i:i+8]))
    except:
            break