"""
48. Rotate Image
"""


class Solution:

    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        height = len(matrix)
        if height == 0:
            return
        width = len(matrix[0])

        # flip
        low,high = 0,height-1
        while low < high:

            for i in range(0,width):
                tmp = matrix[low][i]
                matrix[low][i] = matrix[high][i]
                matrix[high][i] = tmp
            low += 1
            high -= 1

        #diagonally flip
        start_idx = 1
        for i in range(height):
            for j in range(start_idx,width):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
            start_idx += 1