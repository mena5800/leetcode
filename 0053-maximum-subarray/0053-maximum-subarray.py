class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr_2 = []
        for i in range(len(nums)):
            if i ==0:
                arr_2.append(nums[i])
            else:
                arr_2.append(max(nums[i]+arr_2[i-1],nums[i]))
        return max(arr_2)
        