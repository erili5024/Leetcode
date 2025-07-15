# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr1 = []
    def findChild(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        if not root.left and not root.right:
            self.arr1.append(root.val)
            return
        self.findChild(root.left)
        self.findChild(root.right)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.arr1 = []
        self.findChild(root1)
        leaves1 = self.arr1.copy()
        self.arr1 = []
        self.findChild(root2)
        leaves2 = self.arr1.copy()
        if leaves1 == leaves2:
            return True
        else:
            return False