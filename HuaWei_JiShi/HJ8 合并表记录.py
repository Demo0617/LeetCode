n = int(input())
my_dict = {}
for i in range(n):
    l = input()
    key, val = int(l.split()[0]), int(l.split()[1])
    if key in my_dict:
        my_dict[key] += int(val)
    else:
        my_dict[int(key)] = int(val)

for key, val in sorted(my_dict.items()):
    print(key, val)