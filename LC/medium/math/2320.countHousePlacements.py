class Solution:
    def countHousePlacements(self, n: int) -> int:
        f = [1, 2]
        if n > 1:
            for i in range(2, n+1):
                f.append(f[-1] + f[-2])
        return f[n]**2 % (10**9 + 7)

    