class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_pure = ''.join(ch.lower() for ch in s if ch.isalnum())

        return s_pure == s_pure[::-1]