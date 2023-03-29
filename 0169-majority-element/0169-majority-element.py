class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_nums = {}
        
        for num in nums:
            if dict_nums.get(num,None):
                dict_nums[num] += 1
            else:
                dict_nums[num] = 1
        
        max_num = 0
        nums_lenth = len(nums)
        for key in dict_nums:
            if dict_nums[key] > nums_lenth // 2 :
                return key