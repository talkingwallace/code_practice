"""
72. Edit Distance
tag: DP
"""
# class Solution:
#
#     dp = []
#
#     def minDistance(self, word1, word2):
#
#         self.dp = []
#         if len(word1) == 0:
#             return len(word2)
#         elif len(word2) == 0:
#             return len(word1)
#         else:
#             for i in range(len(word1) + 1):
#                 row = [0] * (len(word2) + 1)
#                 self.dp.append(row)
#
#         for i in range(len(word1) + 1):
#             if i == 0:
#                 continue
#             else:
#                 self.dp[i][0] = i
#         for j in range(len(word2) + 1):
#             if j == 0:
#                 continue
#             else:
#                 self.dp[0][j] = j
#
#         word1 = '0'+word1
#         word2 = '0'+word2
#         for i in range(1,len(word1)):
#             for j in range(1,len(word2)):
#                 add_val = 1 if word1[i] != word2[j] else 0
#                 self.dp[i][j] = min(min(self.dp[i-1][j]+1,self.dp[i][j-1]+1),self.dp[i-1][j-1]+add_val)
#
#         return self.dp[len(word1)-1][len(word2)-1]


# optimization: space complexity to O( min(m,n) )
class Solution:

    dp = []

    def minDistance(self, word1, word2):

        short,long = '',''
        if len(word1) > len(word2):
            short = word1
            long = word2
        else:
            short = word2
            long = word1

        self.dp = []
        self.dp.append([0]*(len(short)+1))
        self.dp.append([0]*(len(short)+1))
        for i in range(len(short)+1):
            self.dp[1][i] = i

        short = '0'+short
        long = '0'+long

        for i in range(1,len(long)):

            self.dp.pop(0)
            self.dp.append([0]*(len(short)))
            self.dp[1][0] = i
            for j in range(1,(len(short))):
                if long[i] == short[j]:
                    add_val = 0
                else:
                    add_val = 1

                self.dp[1][j] = min(min(self.dp[0][j]+1,self.dp[1][j-1]+1),self.dp[0][j-1]+add_val)

        return self.dp[1][-1]

if __name__ == '__main__':
    import numpy as np
    sl = Solution()
    rs = sl.minDistance('execution','intention')
    print(np.array(rs))