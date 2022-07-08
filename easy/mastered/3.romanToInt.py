class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }
        res = 0

        for i in range(len(s)):
            if i < len(s) - 1 and map[s[i]] < map[s[i + 1]]:
                res -= map[s[i]]
            else:
                res += map[s[i]]

        return res