class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = set(nums)
        for i in range(len(nums)):
            num = target - nums[i]
            if num in set_nums and i != nums.index(num):
                return [i,nums.index(num)]

            