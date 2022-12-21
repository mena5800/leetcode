class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        list_ = []
        r = len(triangle) 
        list_ = [0] * r
        for x in range (r):
            list_[x] = [] 

        for i in range(len(triangle)-1,-1,-1):
            for j in range(len(triangle[i])):
                if i ==len(triangle)-1:
                    list_[i] = triangle[i].copy()
                    break
                else:
                    list_[i].append(triangle[i][j]+min(list_[i+1][j],list_[i+1][j+1]))
        return list_[0][0]
                    


