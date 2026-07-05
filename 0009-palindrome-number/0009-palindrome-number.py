class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True
        original = x
        y = 0
        while (x > 0):

            last = x % 10
            y = (y * 10) + last

            x //= 10
        return original == y