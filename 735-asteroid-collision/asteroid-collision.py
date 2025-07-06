class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                top = stack[-1]
                if abs(i) > abs(top):
                    stack.pop()
                    continue
                elif abs(i) == abs(top):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(i) 
        return stack
        