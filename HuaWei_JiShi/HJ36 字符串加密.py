def make_dict(s):
    uni_list = []
    for ch in s:
        if ch in uni_list:
            continue
        else:
            uni_list.append(ch)

    full_letter = sorted({chr(ord("A") + i) for i in range(26)})[::-1]
    for l in uni_list:
        full_letter.remove(l.upper())

    encode = {}
    for i in range(len(uni_list)):
        encode[chr(ord("A") + i)] = uni_list[i].upper()
    for i in range(len(uni_list), 26):
        encode[chr(ord("A") + i)] = full_letter.pop()
    return encode


while True:
    try:
        s = input()
        s2 = input()
        ans = []
        encode = make_dict(s)
        for ch in s2:
            ans.append(encode[ch.upper] if ch.isupper() else encode[ch.upper()].lower())
        print("".join(ans))
    except:
        break


