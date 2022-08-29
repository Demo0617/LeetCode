n = int(input())
ans_list = []
for i in range(n):
    ans_list.append([])
cur_num = 0
for i in range(n):
    while i >= 0:
        cur_num += 1
        ans_list[i].append(str(cur_num))
        i -= 1
for l in ans_list:
    print(' '.join(l))