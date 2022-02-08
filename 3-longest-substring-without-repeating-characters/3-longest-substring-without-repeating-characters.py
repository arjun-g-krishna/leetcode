class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp, longest = '', ''     
        for c in s:
            if c in temp:
                temp = temp[temp.index(c)+1:]+c
            else:
                temp += c
                longest = max(longest, temp, key = len)

        return len(longest)
            
            
                
                
