import heapq

class Solution:

    def topKFrequent(self, nums, k):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        kv = sorted(d,key=d.get,reverse=True)
        topk = kv[:k]
        return topk

if __name__ == '__main__':
    s = Solution()
    rs = s.topKFrequent([3,0,1,0],1)



