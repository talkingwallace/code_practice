"""
322. Coin Change
tag: dp
"""
"""
thinking:搜索回溯
"""

class Solution:

    record = {}

    def search(self,target,coins):

        if target < 0:
            return float('inf')
        if not target in self.record:

            coin_num = float('inf')
            for i in coins:
                rs = self.search(target-i,coins)
                if rs < coin_num:
                    coin_num = rs
            self.record[target] = coin_num + 1
        return self.record[target]

    def coinChange(self, coins, amount):

        if len(coins) == 0:
            return -1

        self.record = {}
        for v in coins:
            self.record[v] = 1

        rs = self.search(amount,coins)

        return rs if rs != float('inf') else -1

if __name__ == '__main__':
    print(Solution().coinChange([3,5],7))
