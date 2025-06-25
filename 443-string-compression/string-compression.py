class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        
        while read < len(chars):
            current_char = chars[read]
            count = 1
            
            while read + 1 < len(chars) and chars[read + 1] == current_char:
                read += 1
                count += 1
            
            chars[write] = current_char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
            read += 1
        
        return write
