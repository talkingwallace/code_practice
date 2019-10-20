"""
84. Largest Rectangle in Histogram
解题思路: https://frezc.github.io/2019/05/25/leetcode-largest-rectangle-in-histogram/
要点: 每个柱子，必定有以其伟最小高度组成的最大面积矩阵
      只要对于每个柱子，找出以其伟最小高度的最大面积矩阵，就可以找出最大面积了
"""

class Solution:

    # DP solution
    def largestRectangleArea(self, heights):
        if len(heights) == 0:
            return 0

        # left boundary
        dp_left = [0]*len(heights)
        dp_left[0] = -1
        for idx in range(1,len(heights)):

            l_idx = idx-1
            l_h = heights[l_idx]
            cur_h = heights[idx]
            while l_h >= cur_h: # <=，等于也可以向右传播
                l_idx = dp_left[l_idx]
                if l_idx == -1:
                    break
                l_h = heights[l_idx]
            dp_left[idx] = l_idx

        # right boundary
        dp_right = [0]*len(heights)
        dp_right[-1] = len(dp_right)
        for idx in reversed(range(0,len(heights)-1)):

            r_idx = idx + 1
            r_h = heights[r_idx]
            cur_h = heights[idx]
            while r_h >= cur_h: # >=，等于也可以向右传播
                r_idx = dp_right[r_idx]
                if r_idx == len(heights):
                    break
                r_h = heights[r_idx]
            dp_right[idx] = r_idx

        max = 0
        for idx in range(len(heights)):
            area = (dp_right[idx] - dp_left[idx] - 1) * heights[idx]
            if area > max:
                max = area

        return max

    # Stack Solution
    # def largestRectangleArea_(self, heights):
    #     if len(heights) == 0:
    #         return 0
    #
    #     max_area = 0
    #     stack = []
    #     for idx,num in enumerate(heights):
    #         if idx == 0:
    #             stack.append(idx)
    #             continue
    #         while num < stack[-1]:
    #             h = heights[stack.pop()]
    #             l = -1 if len(stack) == 0 else stack[-1]
    #             r = idx
    #             area = (r-l-1)*h
    #             if area > max_area:
    #                 max_area = area
    #
    #         stack.append(idx)
    #
    #     return max_area


print(Solution().largestRectangleArea_([2,1,5,6,2,3]))