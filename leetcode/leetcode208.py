"""
208. Implement Trie (Prefix Tree)
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = {}
        self.end_node = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self._insert(word,0)

    def _insert(self,word,cur_idx):
        if cur_idx == len(word):
            self.end_node = True
            return
        c = word[cur_idx]
        if c not in self.next:
            self.next[c] = Trie()
        self.next[c]._insert(word,cur_idx+1)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self._search(word,0)

    def _search(self,word,cur_idx,mode='all'):

        if cur_idx == len(word):
            return self.end_node if mode == 'all' else True

        c = word[cur_idx]
        if c in self.next:
            return self.next[c]._search(word,cur_idx+1,mode)

        return False

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix,cur_idx=0,mode='prefix')

root = Trie()
root.insert('apple')
print(root.startsWith('app'))
root.insert('app')
