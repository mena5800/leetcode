class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = {}
        for i in range(97,123):
            dict_[chr(i)] = i
        
        def hash_function(str_,dict_):
            sum = 1
            for i in range(len(str_)):
                sum *= (dict_[str_[i]] ** 3 - dict_[str_[i]])
            return sum

                
        nums = []
        for word in strs:
            nums.append(hash_function(word,dict_))
        dict_1 = {}
        
        for i in range(len(nums)):
            num = dict_1.get(nums[i],-10)
            if num == -10:
                dict_1[nums[i]] = [strs[i]]
            else:
                dict_1[nums[i]].append(strs[i])
                
        return dict_1.values()
        
            
            
        
