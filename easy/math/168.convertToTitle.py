class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''

        while columnNumber:
            a = columnNumber % 26
            if a == 0:
                a = 26
                columnNumber -= 26
            columnNumber = columnNumber // 26
            res += chr(a + ord('A') - 1)

        return res[::-1]