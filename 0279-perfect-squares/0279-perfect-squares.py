class Solution:
    def numSquares(self, n: int) -> int:
        list_ = [n]*(n+1)
        list_[0] = 0

        for i in range(1,n+1):
            for j in range(1,i+1):
                square = j * j
                if i - square < 0:
                    break
                list_[i]= min(list_[i],1 + list_[i-square])
        return list_[-1]
                
                

        