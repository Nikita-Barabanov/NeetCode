from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre_val, valid = -2**31 - 1, True

        def infix(node: Optional[TreeNode]) -> None:
            nonlocal pre_val, valid
            if node.left:
                infix(node.left)
            if node.val <= pre_val:
                valid = False
            else:
                pre_val = node.val
            if node.right:
                infix(node.right)

        infix(root)
        return valid


s = Solution()
root = TreeNode(val=5, left=TreeNode(val=1), right=TreeNode(val=4, left=TreeNode(3), right=TreeNode(6)))
s.isValidBST(root)
