class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        if(len < 2) return s;        
        boolean dp[] = new boolean[len];
        int start = 0;
        int maxLen = 0;
        
        for(int i = len - 1; i >= 0; i--){
            for(int j = len - 1; j >= i; j--){
                dp[j] = (s.charAt(i) == s.charAt(j)) && (j - i < 2 || dp[j - 1]);
                if(dp[j] && maxLen <= j - i + 1){
                    start = i;
                    maxLen = j - i + 1;
                }
            }
        }
        return s.substring(start, start + maxLen); 
    }
}