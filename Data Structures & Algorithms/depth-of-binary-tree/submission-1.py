class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the node is None, depth is 0
        if root is None:
            return 0
        
        # Recursive step: Depth = 1 (current node) + max(depth of left, depth of right)
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)
