class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        nums = []
        nums_dict = {}
        for i in range(len(s)):
            if i == 0:
                nums.append(1)
                nums_dict[s[i]] = i
            else:
                if s[i] == s[i-1]:
                    nums.append(1)
                    nums_dict[s[i]] = i
                else:
                    flag = nums_dict.get(s[i],-10)
                    if flag == -10:
                        nums.append(nums[i-1] + 1)
                        nums_dict[s[i]] = i
                    else:
                        nums.append(min(nums[i-1] + 1 , i - nums_dict[s[i]]))
                        nums_dict[s[i]] = i
        return max(nums)
                
        