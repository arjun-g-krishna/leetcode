## Brute force approach

Brute force approach is to try forming words from the string s by taking letters one by one and checking whether that word exists in the dictionary or not

Once we find the matching word we are faced with the problem of checking whether we can break up the rest of the string into words from our dictionary

## A better solution

A better approach would be to check every word in the dictionary. For example the string is leetcode and the dictionary is <br> wordDict = { "leet" , "code" }

We check whether the first four characters in the string is leet, which is true. Then we check the next four characters is leet, which is false, so we check whether the next four characters is code, which is true.

We return true if we reach the last index at some point
