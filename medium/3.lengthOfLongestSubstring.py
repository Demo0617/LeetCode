class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = set()
        left = 0
        max_l = 0
        cur_l =0
        for i in range(len(s)):
            cur_l += 1
            while s[i] in map:
                map.remove(s[left])
                cur_l -= 1
                left += 1
            if cur_l > max_l:
                max_l = cur_l
            map.add(s[i])
        return max_l