class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])

        str_ = "".join(digits)
        num = int(str_) +1
        str_ = str(num)
        list_ = []
        for i in range(len(str_)):
            list_.append(int(str_[i]))
        return list_
