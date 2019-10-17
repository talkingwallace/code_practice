"""
560. Subarray Sum Equals K
相似题目: Leetcode-437
"""

# TLE
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             cur_sum = 0
#             cur_sum += nums[i]
#             if cur_sum == k:
#                 count += 1
#             for j in range(i + 1, len(nums)):
#                 cur_sum += nums[j]
#                 if cur_sum == k:
#                     count += 1
#
#         return count

class Solution:

    # subarr[3:10]和值等于subarr[0:10] - subarr[0:3]
    def subarraySum(self, nums, target) -> int:

        if len(nums) == 0:
            return 0
        count = 0
        record = {0:1}
        sum = 0
        for idx,num in enumerate(nums):
            sum += num
            k = sum - target
            if k in record:
                count += record[k]
            if sum not in record:
                record[sum] = 1
            else:
                record[sum] += 1

        return count

print(Solution().subarraySum([1,1,1],2))