class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        char_word = {}
        
        if len(words) != len(pattern):
            return False
        
        if len(set(words)) != len(set(list(pattern))):
            return False
        
        for i in range(len(pattern)):
            if char_word.get(pattern[i], None):
                continue
            else:
                char_word[pattern[i]] = words[i]
        
        string = ""
        
        for i in range(len(pattern)):
            if i != len(pattern) - 1:
                string += (char_word[pattern[i]] + " ")
            else:
                string += char_word[pattern[i]]
        
        if string == s:
            return True
        else:
            return False