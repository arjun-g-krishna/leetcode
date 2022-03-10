class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialise the result to the first value in the array
        maxSub = nums[0]
        # Initialise currentsum
        curSum = 0
        # Iterate through each number
        for num in nums:
            # If we have a negative value up untill now, we remove it from the sum
            if curSum < 0:
                curSum = 0 # reinitialise current sum to zero in that case
            curSum += num 
            maxSub = max(maxSub,curSum)
        return maxSub