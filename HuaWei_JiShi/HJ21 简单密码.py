def change_l(ch):
    if ch in 'abc':
        return '2'
    elif ch in 'def':
        return '3'
    elif ch in 'ghi':
        return '4'
    elif ch in 'jkl':
        return '5'
    elif ch in 'mno':
        return '6'
    elif ch in 'pqrs':
        return '7'
    elif ch in 'tuv':
        return '8'
    else:
        return '9'


while True:
    try:
        ans = ''
        s = input()
        for ch in s:
            if ch.isdigit():
                ans += ch
            elif ch == ch.upper():
                if ch != 'Z':
                    ans += chr(ord(ch.lower()) + 1)
                else:
                    ans += 'a'
            else:
                ans += change_l(ch)
        print(ans)
    except:
        break


