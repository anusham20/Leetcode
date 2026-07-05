class Solution(object):

    def frequency(self, nums):
        """
        :type nums: List[int]
        :rtype: Dict[int]
        """
        # Getting the number of values in a dictionary is O(n)
        N = {}
        for n in nums:
            if n not in N:
                N[n] = 1
            else:
                N[n] += 1
        return N

    def hashMap (self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: Dict[int]
        """
        # Converting a list to a dictionary is O(n)
        N = {}
        for n in nums:
            N[n] = target - n
        print(N)
        return N
    
    def keyValuePair (self, nums, N):
        """
        :type nums: List[int]
        :type N: Dict[int]
        :rtype: Tuple[int],(Tuple[int])
        """
        # Iterating through dictionary is O(n), 
        # but searching for value as a key in the dictionary is O(1)
        # .get is O(1) in dictionaries
        freq = self.frequency(nums)
        for k in N:
            v = N[k]
            if v in N:
                if v != k:
                    return (k, v)
                if freq.get(v) > 1:
                    return (k, v)

        return (-1, -1)


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # It is O(n) as looking for a value in a list is O(n)
        N = self.hashMap(nums, target)
        k, v = self.keyValuePair(nums, N)
        first = -1
        for i in range(len(nums)):
            if k == nums[i]:
                first = i
                break
        
        second = -1
        for j in range(len(nums)):
            if v == nums[j] and j != first:
                second = j
                break

        return [first, second]      