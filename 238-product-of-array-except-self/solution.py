// 27 ms | 20.3 MB
class Solution(object):
    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            output[i] = product
            product = product * nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * product
            product = product * nums[i]
        return output