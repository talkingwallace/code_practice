"""
437. Path Sum III
相似题目 Leetcode-560
"""
from leetcode.public_class import TreeNode

class Solution:
    val_map = {}
    sum = 114514
    count = 0
    node_idx = 0

    def preorder(self, node):

        if not node:
            return
        self.node_idx += 1

        for k in self.val_map:
            new_val = self.val_map[k] + node.val
            self.val_map[k] = new_val
            if new_val == self.sum:
                self.count += 1

        cur_idx = self.node_idx
        self.val_map[cur_idx] = node.val
        if node.val == self.sum:
            self.count += 1

        self.preorder(node.left)
        self.preorder(node.right)

        self.val_map.pop(cur_idx)
        for k in self.val_map:
            self.val_map[k] = self.val_map[k] - node.val

    def pathSum(self, root: TreeNode, sum):

        if not root:
            return 0

        # initialize
        self.val_map = {}
        self.sum = sum
        self.count = 0
        self.node_idx = 0

        self.preorder(root)

        return self.count