"""
139. Word Break
"""
class Solution:
    def wordBreak(self, s, wordDict):

        if len(s) == 0:
            return True
        if len(wordDict) == 0:
            return False

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for idx in range(len(s)+1):

            for w in wordDict:
                if len(w) <= idx and dp[idx - len(w)] and s[idx-len(w):idx] == w:
                    dp[idx] = True

        return dp[-1]


print(Solution().wordBreak("applepenapple",['apple','penf']))
