from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Неправильно
        nodes = [root]
        for node in nodes:
            if node.left:
                if node.left.val >= node.val:
                    return False
                nodes.append(node.left)
            if node.right:
                if node.right.val <= node.val:
                    return False
                nodes.append(node.right)

        return True
