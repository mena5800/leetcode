class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        dict_ = {}
        dict_ ={"0":0,"1":1}
        for i in range(2,n+1):
            binary = format(i,'b')
            key = binary[1:]
            key = key.strip(".0")
            if key == "":
                dict_[binary] = 1
            else:
                dict_[binary] = 1 + dict_[key]
        result = []
        for key in dict_:
            result.append(dict_[key])
        return result
            
          