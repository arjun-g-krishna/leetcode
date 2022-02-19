class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        for i in range(1, len(nums)):
            if nums[i] != 0:                
                nums[i] += nums[i-1]             
        return max(nums)