class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        stack = []
        for ch  in s:
            if ch in mapping:
                stack.append(ch)
            elif stack:
                item = stack.pop()
                if mapping[item] != ch:
                    return False
            else:
                return False
        return not stack                



