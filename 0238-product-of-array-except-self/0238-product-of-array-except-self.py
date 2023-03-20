class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        postfix = [nums[0]] * len(nums)
        prefix = [nums[-1]] * len(nums)
        
        for i in range(1,len(nums)):
            postfix[i] = nums[i] * postfix[i-1]
            
        for i in range(len(nums)-2,-1,-1):
            prefix[i] = nums[i] * prefix[i+1]
        
        for i in range(len(nums)):
            if i == 0:
                nums[i] = prefix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = postfix[i - 1]
            else:
                nums[i] = prefix[i + 1] * postfix[i - 1]
                
        return nums



            
            
