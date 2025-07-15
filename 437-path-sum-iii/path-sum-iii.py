# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    def findSum(self, root: Optional[TreeNode], targetSum: int, possible: List[int]) -> None:
        if not root:
            return
        i = 0 
        temp = []
        while i < len(possible):
            temp.append(possible[i] + root.val)
            i += 1 
        temp.append(root.val) 
        self.total += temp.count(targetSum)
        self.findSum(root.right, targetSum, temp)
        self.findSum(root.left, targetSum, temp)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int: 
        possible = []
        self.findSum(root, targetSum, possible)
        return self.total


        