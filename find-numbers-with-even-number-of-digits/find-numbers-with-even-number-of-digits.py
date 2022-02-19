class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if(num>9  and num <100):
                count = count + 1
            elif(num>999 and num< 10000):
                count = count + 1
            elif(num>99999 and num<1000000):
                count = count+1
        return count         