// 287 ms | 13.2 MB
class Solution(object):
    def isPalindrome(self, s):
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()
        return new == new[::-1]

        