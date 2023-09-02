from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        q, nodes = deque([root, ]), []
        while q:
            cur_node = q.popleft()
            if cur_node:
                nodes.append(str(cur_node.val))
                q.append(cur_node.left)
                q.append(cur_node.right)
            else:
                nodes.append("_")

        return ",".join(nodes)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        nodes = deque(data.split(","))
        root= TreeNode(int(nodes.popleft()))
        q = deque([root, ])
        while q:
            cur_node = q.popleft()
            if (left := nodes.popleft()) != "_":
                cur_node.left = TreeNode(int(left))
                q.append(cur_node.left)

            if (right := nodes.popleft()) != "_":
                cur_node.right = TreeNode(int(right))
                q.append(cur_node.right)

        return root




# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans