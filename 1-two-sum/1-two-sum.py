class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary that stores the previous elements that we traversed
        prevMap = {} # Stored in the form value:index
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return       
