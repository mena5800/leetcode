class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        my_dict = {'b':0,'a':0,'l':0,'o':0,'n':0}
        
        for i in range(len(text)):
            if my_dict.get(text[i],-10) != -10 :
                my_dict[text[i]] += 1
                
        counter1 = min(my_dict['a'],my_dict['b'],my_dict['n'])
        counter2 = min(my_dict['l'],my_dict['o'])
        
        if counter1 * 2 <= counter2:
            return counter1
        else:
            return counter2 // 2 if counter1 > counter2 // 2 else 0
                