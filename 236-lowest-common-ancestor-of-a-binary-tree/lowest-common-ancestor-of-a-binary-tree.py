class Solution:
    def ifChild(self, root: 'TreeNode', value: int, memo: dict) -> bool:
        if not root:
            return False
        if root.val == value:
            return True
        if (root, value) in memo:
            return memo[(root, value)]
        found = self.ifChild(root.left, value, memo) or self.ifChild(root.right, value, memo)
        memo[(root, value)] = found
        return found

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque()
        queue.append(root)
        prev = root
        memo = {}

        while queue:
            node = queue.popleft()
            if node.val == p.val:
                if self.ifChild(node, q.val, memo):
                    return node
            elif node.val == q.val:
                if self.ifChild(node, p.val, memo):
                    return node
            elif self.ifChild(node, p.val, memo) and self.ifChild(node, q.val, memo):
                queue = deque()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return prev