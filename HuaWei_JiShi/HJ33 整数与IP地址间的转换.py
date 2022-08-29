while True:
    try:
        ans = ''
        list_1 = input().split('.')
        for ch in list_1:
            ch2bin = bin(int(ch))[2:]
            ch2bin = '0' * (8 - len(ch2bin)) + ch2bin
            ans += ch2bin
        ans = int(ans, 2)
        print(ans)

        num_2 = bin(int(input()))[2:]
        num_2 = '0' * (32 - len(num_2)) + num_2
        ans_list = []
        for start in range(4):
            num = num_2[start * 8: start * 8 + 8]
            num = str(int(num, 2))
            ans_list.append(num)
        print('.'.join(ans_list))
    except:
        break