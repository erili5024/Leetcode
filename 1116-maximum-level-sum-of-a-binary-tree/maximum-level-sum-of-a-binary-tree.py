# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        maxed = -1000000
        levels = 1
        queue.append([root, 1])
        sum = 0 
        while queue:
            temp = queue.popleft()
            node = temp[0]
            level = temp[1]
            sum += node.val
            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])
            if not queue or level != queue[0][1]:
                if sum > maxed:
                    maxed = sum 
                    levels = level
                sum = 0
        return levels