class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        ans = strs[0]

        for i in range(len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(ans) and ans[j] == strs[i][j]:
                j += 1
            if j == 0:
                return ''
            ans = ans[:j]

        return ans