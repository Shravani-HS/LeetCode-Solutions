// 17 ms | 12.4 MB
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        for char in t:
            count[ord(char) - ord('a')] -= 1

        for x in count:
            if x != 0:
                return False

        return True