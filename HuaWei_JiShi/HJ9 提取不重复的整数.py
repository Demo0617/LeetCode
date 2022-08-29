my_list = []
while True:
    try:
        s = input()
        s = s[::-1]
        for i in s:
            if i in my_list:
                continue
            else:
                my_list.append(i)
                print(i, end='')
    except:
        break

