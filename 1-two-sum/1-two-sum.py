class Solution(object):
    def twoSum(self, nums, target):
        dicts = {}
        for i in range(len(nums)):
            if nums[i] in dicts.keys():
                return [dicts[nums[i]],i]
            else:
                dicts[target - nums[i]] = i
        return [0,0]                