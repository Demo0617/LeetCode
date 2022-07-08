class Solution:
    def climbStairs(self, n):
        if n == 1: return 1
        if n == 2: return 2
        help = [0] * n
        help[0] = 1
        help[1] = 2
        for i in range(2,n):
            help[i] = help[i-1] + help[i-2]
        return help[-1]