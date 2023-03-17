class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_dp = [1] * len(nums)
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] - 1 == nums[i-1]:
                nums_dp[i] = nums_dp[i-1] + 1
            if nums[i] == nums[i-1]:
                nums_dp[i] = nums_dp[i-1]
        return max(nums_dp)
                