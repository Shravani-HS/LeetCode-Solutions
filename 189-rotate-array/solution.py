// 28 ms | 28.8 MB
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums1 = nums[-k:]
        nums2 = nums[:-k]
        nums[:] = nums1+nums2
        return nums
            