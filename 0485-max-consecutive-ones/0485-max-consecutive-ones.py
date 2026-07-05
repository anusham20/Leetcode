class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        bestCount = 0
        count = 0
        i = 0
        while (i < len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            
            if bestCount < count:
                bestCount = count
            i += 1
        return bestCount