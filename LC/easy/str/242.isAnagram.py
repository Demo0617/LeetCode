class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = collections.Counter(s)
        map2 = collections.Counter(t)

        return map1 == map2