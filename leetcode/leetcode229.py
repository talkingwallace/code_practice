"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

tag: boyer-moore voting
原理：对于一个序列共有m个，同时消去n个，则余下的元素超过floor(m/n)

"""
import math
class Solution:

    def majorityElement(self, nums):

        if len(nums) == 0:
            return None

        holder1,holder2 = 0,0
        count1,count2 = 0,0
        target_val = math.floor(len(nums)/3)

        for num in nums:

            if count1 == 0 and num != holder2:
                holder1 = num
                count1 += 1
                continue

            elif count2 == 0 and num != holder1:
                holder2 = num
                count2 += 1
                continue

            if num == holder1:
                count1 += 1
            elif num == holder2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1,count2 = 0,0
        for num in nums:
            if num == holder1:
                count1 += 1
            elif num == holder2:
                count2 += 1

        rs = []
        if count1 > target_val:
            rs.append(holder1)
        if count2 > target_val:
            rs.append(holder2)

        return rs

if __name__ == '__main__':
    print(Solution().majorityElement([1,2,2,3,2,1,1,3]))
