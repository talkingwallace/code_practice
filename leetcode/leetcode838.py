"""
838. Push Dominoes
thinking: 多次遍历直到状态稳定
"""

class Solution:

    # wrong code
    # def pushDominoes(self, dominoes):
    #
    #     if len(dominoes) == 0:
    #         return dominoes
    #
    #     while True:
    #         status_change = False
    #
    #         """
    #         .L.R...LR..L..
    #         """
    #         dominoes = list(dominoes)
    #         for idx,p in enumerate(dominoes):
    #
    #             if p == 'L':
    #                 if idx-1 >= 0:
    #                     if dominoes[idx-1] == 'L' or dominoes[idx-1] == 'R':
    #                         continue
    #                     else:
    #                         if idx-2 > 0 and dominoes[idx-2] != 'R':
    #                             dominoes[idx-1] = 'L'
    #                             status_change = True
    #                         elif idx - 2 <= 0:
    #                             dominoes[idx-1] = 'L'
    #                             status_change = True
    #
    #             elif p == 'R':
    #                 if idx+1 < len(dominoes):
    #                     if dominoes[idx+1] == 'L' or dominoes[idx+1] == 'R':
    #                         continue
    #                     else:
    #                         if idx + 2 < len(dominoes) and dominoes[idx+2] != 'L':
    #                             dominoes[idx+1] = 'R'
    #                             status_change = True
    #                         elif idx + 2 >= len(dominoes):
    #                             dominoes[idx+1] = 'R'
    #                             status_change = True
    #
    #         if not status_change:
    #             break
    #
    #     s = ''
    #     for i in dominoes:
    #         s += i
    #     return s

    # the clever answer
    def pushDominoes(self, dominoes):

        if len(dominoes) == 0:
            return

        while True:
            trend = [0]*len(dominoes)
            dominoes = list(dominoes)
            for idx,p in enumerate(dominoes):
                if p == 'L' and idx-1 >= 0:
                    if dominoes[idx-1] == '.':
                        trend[idx-1] -= 1
                if p == 'R' and idx+1 < len(dominoes):
                    if dominoes[idx+1] == '.':
                        trend[idx+1] += 1


            flag = False

            for idx,val in enumerate(trend):
                if val >= 1:
                    dominoes[idx] = 'R'
                    flag = True
                elif val <= -1:
                    dominoes[idx] ='L'
                    flag = True

            if not flag:
                break

        s = ''
        for i in dominoes:
            s += i
        return s

if __name__ == '__main__':
    s = Solution()
    rs = s.pushDominoes('R...L')