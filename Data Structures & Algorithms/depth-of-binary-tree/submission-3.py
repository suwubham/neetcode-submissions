# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Goal: store the depth of each iteration until we reach null
        max_depth = 0
        if not root:
            return max_depth
        
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            print(f"Current Node: {node.val} Current Depth: {depth}")
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
            

        
        return max_depth
 
        