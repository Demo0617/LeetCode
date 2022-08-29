class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n: return False
        map1 = {}
        map2 = {}
        for i in range(m):
            if s[i] in map1.keys() and t[i] in map2.keys() and t[i] == map1[s[i]] and s[i] == map2[t[i]]:
                continue
            elif s[i] not in map1.keys() and t[i] not in map2.keys():
                map1[s[i]] = t[i]
                map2[t[i]] = s[i]
            else:
                return False

        return True