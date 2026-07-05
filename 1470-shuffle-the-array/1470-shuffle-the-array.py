class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = []
        i = 0
        while i < (len(nums))//2:
            nums2.append(nums[i])
            nums2.append(nums[i + len(nums)//2])
            i += 1
        
        return nums2