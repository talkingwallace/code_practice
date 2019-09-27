class Solution:

    def lengthOfLIS(self, nums:list):

        if len(nums) == 0:
            return 0

        dp = [0]*len(nums)

        dp[0] = 1
        rs = -1

        for idx in range(1, len(nums)):

            maxLen = 1
            for k in range(0,idx):
                if nums[idx] > nums[k]:
                    maxLen = max(maxLen,dp[k]+1)
            dp[idx] = maxLen
            if maxLen > rs:
                rs = maxLen

        return rs


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))