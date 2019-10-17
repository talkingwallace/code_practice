"""
79. Word Search
"""
class Solution:

    flag = False

    def search(self,x,y,word,idx,board,visited):

        if x < 0 or x >= len(board):
            return
        if y < 0 or y >= len(board[0]):
            return
        if visited[x][y]:
            return
        if board[x][y] != word[idx]:
            return
        if self.flag:
            return

        idx += 1
        if idx == len(word):
            self.flag = True
            return
        visited[x][y] = True
        self.search(x+1,y,word,idx,board,visited)
        self.search(x-1,y,word,idx,board,visited)
        self.search(x,y-1,word,idx,board,visited)
        self.search(x,y+1,word,idx,board,visited)
        visited[x][y] = False


    def exist(self, board, word: str):

        if len(word) == 0 or len(board) == 0:
            return False

        self.flag = False
        visited = []
        for i in range(len(board)):
            visited.append([False]*len(board[0]))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.search(i,j,word,0,board,visited)
                if self.flag:
                    break

        return self.flag

print(Solution().exist([["a","a"]],"aaa"))
