class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == [""]: return [[""]]

        result = []
        hashMap = {}
        
        for word in strs:
            w = str(sorted(word))
            if w not in hashMap:
                hashMap[w] = [word]
            else:
                hashMap[w].append(word)
        
        for k in hashMap:
            v = hashMap[k]
            result.append(v)
        return result
            