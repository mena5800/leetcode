class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True if  1 >= n else False
            else:
                return True if n == 0 else False
            
        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i] == flowerbed[i+1]:
                    counter += 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == flowerbed[i-1]:
                    counter += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i] == flowerbed[i-1] and flowerbed[i] == flowerbed[i+1]:
                    counter += 1
                    flowerbed[i] = 1
        return True if counter >= n else False 
                    

        