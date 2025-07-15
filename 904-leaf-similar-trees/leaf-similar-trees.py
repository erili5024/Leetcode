# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr1 = []
    def findChild(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0  
        left = self.findChild(root.left)
        right = self.findChild(root.right)

        if left == 0 and right == 0:
            self.arr1.append(root.val)

        return 1  
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