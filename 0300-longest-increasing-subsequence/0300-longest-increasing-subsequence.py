class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        list_ = []
        for i in range(len(nums)):
            max_ =1
            cond = False
            if i == 0:
                list_.append(1)
            else:
                for j in range(i):
                    if nums[i] > nums[j]:
                        max_ = max(max_,list_[j])
                        cond = True
                if cond:
                    list_.append(max_+1)
                else:
                    list_.append(max_)
        return max(list_)
                
                    