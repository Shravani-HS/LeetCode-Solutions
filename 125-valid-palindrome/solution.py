// 239 ms | 13.1 MB
class Solution(object):
    def isPalindrome(self, s):
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()
        if new == new[::-1]:
            return True
        return False