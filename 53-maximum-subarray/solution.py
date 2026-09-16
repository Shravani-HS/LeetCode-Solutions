// 15 ms | 22 MB
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        if l == 1:
            return nums[0]
        
        m = nums[0]
        sum = 0
        for i in nums:
            sum += i
            if i>sum:
                sum = i
            if sum > m:   
                m = sum
        return m