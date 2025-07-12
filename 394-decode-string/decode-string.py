class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr = ""
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((curr, num))
                curr = ""
                num = 0
            elif char == "]":
                temp = stack.pop()
                prev = temp[0]
                repeat = temp[1]
                curr = prev + curr * repeat
            else:
                curr += char
        return curr

        