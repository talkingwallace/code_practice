"""
279. Perfect Squares
"""
import math
class Solution:

    record = {0:1,1:1,2:2,3:3,4:1,5:2,6:3,7:4,8:2,9:1}

    def search(self,num):
        if num in self.record:
            return self.record[num]

        if type(math.sqrt(num)) is int:
            self.record[num] = 1
            return 1



    def numSquares(self, n):
        return self.search(n)