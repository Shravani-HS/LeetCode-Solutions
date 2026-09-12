// 35 ms | 18.3 MB
class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
        