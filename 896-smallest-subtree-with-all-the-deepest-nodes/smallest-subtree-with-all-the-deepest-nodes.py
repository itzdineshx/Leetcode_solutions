# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        1. Find the depth of every nodes
        2. Find the answer with the help of depth
            * node is deepest of depth -> candiate
            * both children is candidate -> parent is answer
        """
        depth = {None: -1} # Intialize the depth

        # Depth First Search(for deepest Node)
        def dfs(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        max_depth = max(depth.values()) # deep depth (max)

        def ans(node):
            # return the max candidates at deepest depth
            if not node or depth.get(node) == max_depth:
                return node
            left = ans(node.left)
            right = ans(node.right)

            if left and right: return node
            if left : return left
            if right : return right
            
            return None

        return ans(root)