class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_xor = 0
        for num in nums:
            num_xor ^= num
        return num_xor
            