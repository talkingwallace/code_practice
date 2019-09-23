"""
0 - 1 背包
"""

def _01pack(weights:list,values:list,capacity:int):

    assert len(weights) == len(values)
    kv = list(zip(weights,values))
    kv = sorted(kv,key=lambda x:x[0])
    kv.insert(0,(0,0))

    dp = []
    for i in range(len(kv)):
        dp.append([0]*(capacity+1))

    for i in range(len(kv)):

        for j in range(capacity+1):

            if kv[i][0] > j:
                dp[i][j] = dp[i][j-1]
            elif kv[i][0] <= j:
                dp[i][j] = max(dp[i-1][j-kv[i][0]]+kv[i][1],dp[i][j-1])

    return dp
    

if __name__ == '__main__':
    print('hello world')
    import numpy as np
    rs = _01pack([1,2,5,6,7],[1,6,18,22,28],15)
    print(np.array(rs))
