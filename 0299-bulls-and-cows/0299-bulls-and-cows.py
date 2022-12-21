class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n_bulls = 0
        dict_1 = {}
        dict_2 = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                n_bulls +=1
            else:
                if secret[i] not in dict_1:
                    dict_1[secret[i]] = 1
                else:
                    dict_1[secret[i]] +=1
                if guess[i] not in dict_2:
                    dict_2[guess[i]] =1
                else:
                    dict_2[guess[i]] +=1
            n_cows = 0
            for key in dict_1:
                if dict_2.get(key) != None:
                    n_cows += min(dict_1[key],dict_2[key])
        return f"{n_bulls}A{n_cows}B"

                


        