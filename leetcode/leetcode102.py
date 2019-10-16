from leetcode.public_class import TreeNode

class Solution:

    def levelOrder(self, root: TreeNode):

        if not root:
            return []

        queue = []
        queue.append((root, 0))
        rs = []
        while len(queue) != 0:
            node, lvl = queue.pop(0)
            if lvl + 1 > len(rs):
                rs.append([])
            rs[lvl].append(node.val)
            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))

        return rs

