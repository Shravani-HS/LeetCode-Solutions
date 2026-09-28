// 0 ms | 12.3 MB
class Solution(object):
    def check(self, nums):
        count = 0  
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                count +=1 

        if nums[len(nums)-1] > nums[0]:
            count +=1
        if count >= 2 :
            return False 
        else :
            return True





        