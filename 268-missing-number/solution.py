// 20 ms | 13.3 MB
class Solution(object):
    def missingNumber(self, nums):
        sn = sorted(nums)
        if sn[0] != 0:
            return 0
        for i in range(len(sn) - 1):
            if sn[i] + 1 != sn[i + 1]:
                return sn[i] + 1
        return sn[-1] + 1