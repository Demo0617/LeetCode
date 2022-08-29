while True:
    try:
        n = int(input())
        my_list = []
        for i in range(n):
            s = input()
            my_list.append(s)
        for item in sorted(my_list):
            print(item)
    except:
        break