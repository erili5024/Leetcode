class Solution:
    def isValid(self, word: str) -> bool:
        vowel = 0
        cons = 0
        vowels = ['a','e','i','o','u']
        if len(word) < 3:
            return False
        for i in word:
            if i.lower() not in list(string.ascii_lowercase)+ list(string.digits):
                return False
            if i.lower() in vowels:
                vowel += 1
            elif i.lower() in list(string.ascii_lowercase):
                cons += 1
        if vowel >= 1 and cons >= 1:
            return True
        else:
            return False