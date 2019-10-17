
class trie_node(object):

    def __init__(self,val):
        self.table = {}
        self.end_place = False
        self.val = val

    def build(self,word):
        self._build_helper(word,0)

    def _build_helper(self,word,idx):
        if len(word) == idx:
            self.end_place = True
            return
        char = word[idx]
        if char not in self.table:
            self.table[char] = trie_node(char)

        self.table[char]._build_helper(word,idx+1)

    def find(self,word):
        return self._find_helper(word,0)

    def _find_helper(self,word,idx):
        if len(word) == idx:
            if self.end_place:
                return True
            else:
                return False
        if word[idx] not in self.table:
            return False
        else:
            return self.table[word[idx]]._find_helper(word,idx+1)

def display(root:trie_node):
    if not root:
        return
    print(root.table.keys(),len(root.table),root.val,root.end_place)
    for k in root.table:
        display(root.table[k])

root = trie_node(None)
root.build('caonima')
root.build('nmsl')
root.build('caoni')
root.build('wsngg')
print(root.find('caonima'))