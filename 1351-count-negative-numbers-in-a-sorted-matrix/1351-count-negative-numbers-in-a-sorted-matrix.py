class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total=0 
        for i in grid: 
            l=0 
            r=len(i)-1 
            while l<=r:
                mid=(l+r)//2 
                if i[mid]>=0: 
                    l=mid+1 
                else: 
                    total+=r-mid+1 
                    r=mid-1 
        return total
        