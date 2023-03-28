class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        list_ = [1,2,3]
        for i in range(2,n+1):
            max_num = 0
            m = 1
            for j in range(i,-1,-1):
                max_num = max(max_num,list_[j] * m)
                m += 1
            list_.append(max_num)
        return list_[-3]