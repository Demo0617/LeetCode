s_input = input().split(' ')
n, words, target, k = int(s_input[0]), s_input[1: -2], s_input[-2], int(s_input[-1])

ans = []
for word in words:
    if sorted(target) == sorted(word) and target != word:
        ans.append(word)

print(len(ans))
if len(ans) >= k:
    print(sorted(ans)[k - 1])