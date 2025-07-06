class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        write = 0
        read = 0
        while read < len(s):
            if s[read] == '*':
                if write != 0:
                    write = write - 1
            else:
                s[write] = s[read]
                write += 1
            read += 1
        return ''.join(s[:write])
