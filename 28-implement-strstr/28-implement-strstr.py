class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        length = len(needle)
        for i, val in enumerate(haystack):
            if haystack[i: i+length] == needle:
                return i
        return -1