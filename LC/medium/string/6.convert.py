class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ['' for i in range(numRows)]
        j = 0
        flag = -1

        for i in range(len(s)):
            res[j] += s[i]
            if j == 0 or j == numRows - 1:
                flag = - flag
            j = j + flag
        return ''.join(res)