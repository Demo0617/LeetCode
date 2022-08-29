from collections import Counter
while True:
    try:
        num = str(bin(int(input())))
        c = Counter(num)
        print(c['1'])
    except:
        break