point = [0, 0]
def is_valid(s):
    if not s:
        return False
    if s.startswith('A') or s.startswith('W') or \
        s.startswith('S') or s.startswith('D'):
        if s[1:].isdigit():
            return True
    return False

my_list = input().split(';')
for i in range(len(my_list)):
    if is_valid(my_list[i]):
        step = int(my_list[i][1:])
        if my_list[i].startswith('A'):
            point[0] -= step
        if my_list[i].startswith('D'):
            point[0] += step
        if my_list[i].startswith('S'):
            point[1] -= step
        if my_list[i].startswith('W'):
            point[1] += step
    else:
        continue
print('{},{}'.format(point[0], point[1]))