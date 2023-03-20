class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]] * len(height)
        for i in range(2,len(height)):
            left[i] = max(left[i-1],height[i-1])
        
        right = [height[len(height)-1]] * len(height)
        
        for i in range(len(height)-2,-1,-1):
            right[i] = max(right[i+1],height[i+1])
            
        sum_ = 0
        
        for i in range(len(height)):
            num = min(left[i],right[i]) - height[i]
            if num < 0:
                continue
            else:
                sum_ += num
        return sum_