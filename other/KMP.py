"""
find substring
"""

def make_next(string):

    next = [0]*(len(string)+1)
    next[0] = -1
    i,j = 0,-1

    while(i < len(string)):
        print(next)
        if j == -1 or string[i] == string[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]

    return next

def KML(pattern,string):

    next_ = make_next(string)[:-1]
    i,j = 0,0
    while i<len(string) and j<len(pattern):

        if j == -1 and pattern[i] == string[j]:
            i+=1
            j+=1
        else:
            j = next_[j]

    return j == len(pattern)

print(make_next('abcabcabcacab'))

