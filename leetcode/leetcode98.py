from leetcode.public_class import TreeNode

# key:in_order

class Solution:
    prev = None
    result = True

    def in_order(self, node):

        if not node:
            return
        self.in_order(node.left)
        if self.prev is None:
            self.prev = node.val
        else:
            if node.val <= self.prev:
                self.result = False
                return
            self.prev = node.val
        self.in_order(node.right)

    def isValidBST(self, root: TreeNode):

        if not root:
            return True
        self.prev = None
        self.result = True
        self.in_order(root)
        return self.result