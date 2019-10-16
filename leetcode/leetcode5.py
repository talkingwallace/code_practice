"""
5. Longest Palindromic Substring
"""
import numpy as np
class Solution:

    def countSubstrings(self, s):

        if len(s) == 0:
            return 0

        dp = []
        for i in range(len(s)):
            dp.append([False]*len(s))

        # initialize

        l,r = 0,0

        for i in range(len(s)):
            dp[i][i] = True
            if i + 1 < len(s) and s[i] == s[i+1]:
                dp[i][i+1] = True
                l,r = i,i+1

        for inter in range(2,len(s)):
            end = inter
            for i in range(0,len(s)):
                if end < len(s):
                    dp[i][end] = dp[i+1][end-1] and (s[i] == s[end])
                    if dp[i][end] and (end - i >= r - l):
                        if i != 0 and end != len(s) - 1:
                            l,r = i,end
                    end = end + 1
                else:
                    break

        return s[l:r+1]

print(Solution().countSubstrings('abba'))