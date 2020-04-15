# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dia(root, 0)[1]

    def dia(self, root, d):
        if not root:
            return 0, d
        left, d = self.dia(root.left, d)
        right, d = self.dia(root.right, d)
        return 1 + max(left, right), max(d, left + right)
