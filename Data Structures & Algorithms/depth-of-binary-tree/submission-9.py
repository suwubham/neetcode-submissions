# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        # if not root:
        #     return 0
        # max_depth = 1
        # stack = [(root, max_depth)]
        # while stack:
        #     node, depth = stack.pop()
        #     max_depth = max(depth, max_depth)
        #     if node.left:
        #         stack.append((node.left, depth + 1))
        #     if node.right:
        #         stack.append((node.right, depth + 1))
        
        # return max_depth

        #recursive soln using postorder traversal


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)


        