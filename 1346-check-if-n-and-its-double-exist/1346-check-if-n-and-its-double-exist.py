class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        set_ = set(arr)
        counter0 = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                counter0 +=1
            else:
                if 2*arr[i] in set_:
                    return True
        if counter0 >1:
            return True
        else:
            return False





