# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxed = 0
    #0 is left, 1 is right
    def findLongest(self, root: Optional[TreeNode], direction: int, count: int) -> None:
        if not root:
            return 
        count += 1
        if count > self.maxed:
            self.maxed = count
        if direction == -1:
            self.findLongest(root.left, 0, 0)
            self.findLongest(root.right, 1, 0)
        elif direction == 0:
            self.findLongest(root.right, 1, count)
            self.findLongest(root.left, 0,0)
        elif direction == 1:
            self.findLongest(root.left, 0, count)
            self.findLongest(root.right, 1,0)
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.findLongest(root, -1, -1)
        return self.maxed
        