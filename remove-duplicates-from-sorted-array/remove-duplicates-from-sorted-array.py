class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # This can be done using two pointers. One pointer scans the array from
        # beginning to end. The other one keeps track of where the insertions (of unique values) need           # to take place.
        
        # another problem is to check whether the value that we are currenlty on hasn't been traversed
        
        # Since the array is sorted in ascending order we check the current element and the previous.
        # If these are same, then it is not the first time that we're seeing it.
        k = 1
        for i in range(0,len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[k] = nums[i+1]
                k += 1
        return k          
        