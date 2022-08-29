class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            n = str(n)
            num = 0
            for i in n:
                num = num + int(i) ** 2
            return num

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


