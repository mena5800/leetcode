class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        for i in range(len(nums)):
            if dict_.get(nums[i],None):
                dict_[nums[i]] += 1
            else:
                dict_[nums[i]] = 1
        list_max = []
        for num in range(len(nums) + 1):
            list_max.append([])
        
        for key in dict_:
            list_max[dict_[key]].append(key) 
        
        max_nums = []
        for i in range(len(list_max)- 1,-1,-1):
            if len(list_max[i]) == 0:
                continue
            else:
                for num in list_max[i]:
                    max_nums.append(num)
        return max_nums[0:k]