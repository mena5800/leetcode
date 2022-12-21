class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",
                4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
        list_nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        dict2 = {}
        set1 = set()
        max_num = max(list_nums)
        while True:
            if num>=max_num:
                num -=max_num
                if max_num in set1:
                    dict2[max_num] +=1
                else:
                    dict2[max_num] = 1
                    set1.add(max_num)
                
            else:
                list_nums.remove(max_num)
                max_num = max(list_nums)
            if num ==0:
                break
        keysList = [key for key in dict2]
        str = ""
        for i in keysList:
            num_of_iter = dict2[i] 
            str =str+ dict[i]*dict2[i]
        return str
