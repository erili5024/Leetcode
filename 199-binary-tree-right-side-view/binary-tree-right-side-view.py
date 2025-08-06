# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right = []
        queue = deque()
        queue.append([root, 0])
        while queue:
            temp = queue.popleft()
            node, parent = temp[0],temp[1]
            if node.left:
                queue.append([node.left,parent + 1])
            if node.right:
                queue.append([node.right, parent + 1])
            if not queue or queue[0][1] != parent:
                right.append(node.val)
        return right

        