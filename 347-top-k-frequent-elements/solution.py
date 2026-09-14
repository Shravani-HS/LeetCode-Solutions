// 10 ms | 14 MB
class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        sorted_count = sorted(count, key=count.get, reverse=True)
        return sorted_count[:k]
        