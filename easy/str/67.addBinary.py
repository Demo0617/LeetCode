class Solution(object):
    def addBinary(self, a, b):
        res = ''
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry != 0:
            a_val = int(a[i]) if i >= 0 else 0
            b_val = int(b[j]) if j >= 0 else 0
            num = a_val + b_val + carry
            carry = 1 if num >= 2 else 0
            num = num % 2
            res += str(num)
            i -= 1
            j -= 1
        return res[::-1]