# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    def ifGood(self, root: TreeNode, maxed: int) -> None:
        if not root:
            return
        if(root.val >= maxed):
            self.nodes.append(root)
            maxed = root.val
        self.ifGood(root.left, maxed)
        self.ifGood(root.right, maxed)
    def goodNodes(self, root: TreeNode) -> int:
        self.ifGood(root, -10**4)
        return len(self.nodes)
        