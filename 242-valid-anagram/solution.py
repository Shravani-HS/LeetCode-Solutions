// 27 ms | 13.6 MB
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)