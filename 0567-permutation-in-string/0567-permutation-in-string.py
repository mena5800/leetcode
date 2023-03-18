class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_chars = {}
        for i in range(97,123):
            dict_chars[chr(i)] = i
        
        steps = len(s1)
        sum_s1 = 0
        sum_ = 0
        for i in range(steps):
            sum_s1 += (dict_chars[s1[i]] ** 4 - dict_chars[s1[i]] )
        
        for i in range(0,len(s2) - steps + 1):
            if i == 0:
                for i in range(steps):
                    sum_ += (dict_chars[s2[i]] ** 4 - dict_chars[s2[i]])
            else:
                sum_ -= (dict_chars[s2[i-1]] ** 4 - dict_chars[s2[i-1]])
                sum_ += (dict_chars[s2[i+steps-1]] ** 4 - dict_chars[s2[i+steps-1]])
            if sum_ == sum_s1:
                return True
        else:
            return False
                

                
            


        
