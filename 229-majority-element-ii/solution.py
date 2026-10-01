// 8 ms | 15.1 MB
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        res = []
        for num in count:
            if count[num] > n/3:
                res.append(num)
        return res