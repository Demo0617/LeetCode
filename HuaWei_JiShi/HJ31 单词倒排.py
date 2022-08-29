s = input()
for ch in s:
    if ch.isalnum():
        continue
    else:
        s = s.replace(ch, ' ')
s = s.split()[::-1]
for word in s:
    print(word, end=' ')