while True:
    try:
        n = input()
        my_list = []
        for i in range(int(n)):
            my_list.append(int(input()))
        my_set = set(my_list)
        for j in sorted(my_set):
            print(j)
    except:
        break