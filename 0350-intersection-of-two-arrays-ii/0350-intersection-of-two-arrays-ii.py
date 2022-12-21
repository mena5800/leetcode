class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = len(nums1)
        len2 = len(nums2)
        min_list = []
        max_list = []
        list_ = []
        if len1 < len2:
            min_list = nums1
            max_list = nums2
        else:
            min_list = nums2
            max_list = nums1
        list_ = []
        for i in range(len(min_list)):
            if min_list[i] in max_list:
                list_.append(min_list[i])
                max_list.remove(min_list[i])
        return list_
