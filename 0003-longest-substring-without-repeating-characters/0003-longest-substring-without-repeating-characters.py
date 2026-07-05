class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, uniqueSet = 0, 0, set()
        best = 0
        while (right < len(s) and left <= right):
            if s[right] not in uniqueSet:
                uniqueSet.add(s[right])
                right += 1
                best = max(right - left, best)
            else: 
                uniqueSet.remove(s[left])
                left += 1
        return best
