# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        best = 0

        def height(node):
            nonlocal best
            if not node:
                return -1  # so leaf has height 0 in edges

            left_h = height(node.left)
            right_h = height(node.right)

            # candidate diameter passing through this node
            best = max(best, left_h + right_h + 2)

            # return height of this subtree
            return max(left_h, right_h) + 1

        height(root)
        return best
      