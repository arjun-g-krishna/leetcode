class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #initialise a cache 
        dp = [False]*(len(s)+1) # +1 indicates the base case
        dp[len(s)] = True
        # now traversing the string from the end and working our way towards the beginning
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                # we check if string s has atleast enough characters to be compared to word w
                # Then the second condition compares it. Starting at index i untill i+len(w)
                if(i+len(w)<=len(s) and s[i:i+len(w)] == w):
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
            
        return dp[0]