"""
0 - 1 背包
"""

def _01pack(weights:list,values:list,capacity:int):

    assert len(weights) == len(values)
    kv = list(zip(weights,values))
    kv = sorted(kv,key=lambda x:x[0])

    dp = []
    for i in range(len(kv)):
        dp.append([0]*(capacity+1))

    

if __name__ == '__main__':
    print('hello world')
    kv = _01pack([1,4,6,2],[2,4,1,4],11)
