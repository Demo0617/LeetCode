while True:
    try:
        a = list(input())
        b = list(input())
        ans = ''
        for i in a:
            if i.isupper():
                if i == 'Z':
                    ans += 'a'
                else:
                    ans += chr(ord(i) + 1).lower()
            elif i.islower():
                if i == 'z':
                    ans += 'A'
                else:
                    ans += chr(ord(i) + 1).upper()
            elif i.isdigit():
                if i == '9':
                    ans += '0'
                else:
                    ans += chr(ord(i) + 1)
            else:
                ans += i
        print(ans)

        ans = ''
        for i in b:
            if i.isupper():
                if i == 'A':
                    ans += 'z'
                else:
                    ans += chr(ord(i) - 1).lower()
            elif i.islower():
                if i == 'a':
                    ans += 'Z'
                else:
                    ans += chr(ord(i) - 1).upper()
            elif i.isdigit():
                if i == '0':
                    ans += '9'
                else:
                    ans += chr(ord(i) - 1)
            else:
                ans += i
        print(ans)
    except:
        break
