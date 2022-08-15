class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        cur_l = 0
        max_l = 0
        l, r = 0, 0

        for i in range(len(s)):
            cur_l += 1
            r = i
            while s[i] in lookup:
                lookup.remove(s[l])
                cur_l -= 1
                l += 1
            if cur_l > max_l:
                max_l = cur_l
            lookup.add(s[i])
        return max_l