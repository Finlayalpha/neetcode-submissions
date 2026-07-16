class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True

        def height(node):
            nonlocal balanced

            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                balanced = False

            return 1 + max(left_height, right_height)

        
        if not balanced:
            return balanced
        height(root)
        return balanced