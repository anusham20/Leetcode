class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
        
        buckets = {}
        for num, freq in hashMap.items():
            if freq not in buckets:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)

        print(buckets)
        for n in range(len(nums), -1, -1):
            if n in buckets:
                key = buckets[n]
                for num in key:
                    result.append(num)
        return result[:k]