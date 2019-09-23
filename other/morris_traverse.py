
class TreeNode(object):

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.left.left = TreeNode(7)
tree.right.left.right = TreeNode(8)

def inorder(root):

    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

 # morris 遍历的前中后序
def get_prior(node:TreeNode) -> TreeNode:
    """
    获取中序遍历中的前一个节点
    """
    if not node:
        return None
    else:
        tmp = node.left
        while tmp is not None and tmp.right is not None:
            if tmp.right is node:
                return tmp
            else:
                tmp = tmp.right
        return tmp


def morris_traverse_inorder(root:TreeNode) -> None:

    cur = root
    while cur is not None:

        if cur.left is None:
            print(cur.val)
            cur = cur.right
        else:
            prior = get_prior(cur)
            if prior.right is None:
                prior.right = cur
                cur = cur.left
            else:
                prior.right = None
                print(cur.val)
                cur = cur.right

if __name__ == '__main__':
    inorder(tree)
    print('--------')
    morris_traverse_inorder(tree)

