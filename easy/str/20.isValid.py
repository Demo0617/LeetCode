class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(': ')',
            '[': ']',
            '{': '}',
            '?': '?',
        }

        stack = ['?']
        for ch in s:
            if ch in dic:
                stack.append(ch)
            elif dic[stack.pop()] != ch:
                return False

        return len(stack) == 1