class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0

        for i in range(n):
            temp = ord(columnTitle[i]) - ord('A') + 1
            res = res * 26 + temp
        return res