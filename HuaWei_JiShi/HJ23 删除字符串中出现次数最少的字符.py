from collections import Counter
s = input()
count = Counter(s)
MIN = min(count.values())

for i in s:
    if count[i] == MIN:
        s = s.replace(i,'')
print(s)

