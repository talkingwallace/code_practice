"""
416. Partition Equal Subset Sum
tag: DP
"""
# 回溯法
# TLE
# class Solution:
#
#     flag = False
#
#     def search(self,nums,cur_sum,cur_idx,target_sum):
#
#         if cur_idx >= len(nums):
#             return
#         if self.flag == True:
#             return
#
#         if cur_sum + nums[cur_idx] < target_sum:
#
#             self.search(nums,cur_sum+nums[cur_idx],cur_idx+1,target_sum)
#             self.search(nums,cur_sum,cur_idx+1,target_sum)
#
#         elif cur_sum + nums[cur_idx] == target_sum:
#             self.flag = True
#             return
#         else:
#             self.search(nums,cur_sum,cur_idx+1,target_sum)
#
#     def canPartition(self, nums):
#
#         if len(nums) == 0:
#             return False
#
#         self.flag = False
#         sum = 0
#         for i in nums:
#             sum += i
#
#         # odd or even:
#         if sum & 1 == 1:
#             return False
#         target_sum = int(sum/2)
#
#         self.search(nums,0,0,target_sum)
#         return self.flag

class Solution:

    def canPartition(self, nums):

        pass

if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([2,5,4,2,1]))