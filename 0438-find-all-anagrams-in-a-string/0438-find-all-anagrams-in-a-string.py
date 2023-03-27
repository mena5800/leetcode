class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        dict_chars = {}
        idxs = [] 
        for i in range(97,123):
            dict_chars[chr(i)] = i
        
        def hash_fun(c,dict_chars):
            return (dict_chars[c] ** 3 - dict_chars[c])
        
        num = len(p)
        sum_s = 0
        sum_p = 0
        for i in range(num):
            sum_s += hash_fun(s[i],dict_chars)
            sum_p += hash_fun(p[i],dict_chars)
        
        for i in range(0,len(s) - num + 1):
            if i == 0:
                if sum_s == sum_p:
                    idxs.append(i)
                else:
                    continue
            else:
                sum_s = sum_s - hash_fun(s[i-1],dict_chars) + hash_fun(s[i + num - 1],dict_chars)
                if sum_s == sum_p:
                    idxs.append(i)

        return idxs
                
            
            
            
            