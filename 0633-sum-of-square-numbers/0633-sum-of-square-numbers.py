class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        list_ = []
        i = 0
        while i*i <=c:
            list_.append(i*i)
            i +=1
        
        # there is two numbers equal to c
        set_ = set(list_)
        for i in range(len(list_)):
            target = c - list_[i]
            if target in set_:
                return True
        return False
        