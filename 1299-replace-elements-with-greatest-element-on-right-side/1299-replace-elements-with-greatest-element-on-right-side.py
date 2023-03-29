class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = [0] * len(arr)
        for i in range(len(arr)-1,-1,-1):
            if i == len(arr) - 1:
                max_num[i] = -1
            else:
                max_num[i] = max(max_num[i+1],arr[i+1])
        
        return max_num
            
