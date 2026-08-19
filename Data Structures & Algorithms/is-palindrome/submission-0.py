class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join([char for char in s if char.isalnum()]).lower()
        n = len(st)
        for i in range(int(n / 2)):
            if st[i] != st[n - 1 - i]:
                return False
        return True   