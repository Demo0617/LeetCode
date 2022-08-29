class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[0] * n for i in range(n)]
        left,right,max_len  = 0,0,1
        for i in range(n):
            dp[i][i] = 1
        for r in range(n):
            for l  in range(r):
                if s[r] == s[l] and (dp[l+1][r-1] ==1 or r-l+1<4):
                    dp[l][r] = 1
                    if r-l+1 > max_len:
                        max_len = r-l+1
                        left = l
                        right = r
        return s[left:right+1]