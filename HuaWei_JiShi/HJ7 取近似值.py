n = float(input())
if n - int(n) >= 0.5:
    print(int(n) + 1)
else:
    print(int(n))



#第二种方法

n = float(input())
print(int(n + 0.5))

