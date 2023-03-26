class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list_comb = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                num = nums[i] + nums[start] + nums[end]
                if num > 0:
                    end -= 1
                elif num < 0:
                    start += 1
                else:
                    list_comb.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1] and nums[end] == nums[end + 1]:
                        start += 1
                        end -= 1
                continue
        return list_comb
                    
                    

                
                

                               
                               
                               
                
            
            