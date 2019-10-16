import numpy as np
class Solution:

    def countSubstrings(self, s):

        if len(s) == 0:
            return 0

        dp = []
        for i in range(len(s)):
            dp.append([False]*len(s))

        # initialize

        count = 0

        for i in range(len(s)):
            dp[i][i] = True
            count += 1
            if i + 1 < len(s) and s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1

        for inter in range(2,len(s)):
            end = inter
            for i in range(0,len(s)):
                if end <len(s):
                    dp[i][end] = dp[i+1][end-1] and (s[i] == s[end])
                    if dp[i][end]:
                        count += 1
                    end = end + 1
                else:
                    break

        return count

print(Solution().countSubstrings('abccbaaaab'))