class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = s.lower()
        str_ = ""
        for letter in string:
            num = ord(letter)
            if (num >= 97 and num <= 122) or (num >= 48 and num <= 57):
                str_ += letter
                
        i = 0
        j = len(str_) - 1

        while (i <= j):
            if str_[i] == str_[j]:
                i += 1
                j -= 1
            else:
                return False

        
        return True
        
        
