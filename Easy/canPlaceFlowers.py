# Time complexity: O(n)
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        placed = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if (i == (len(flowerbed) - 1)) and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                placed += 1
            elif i == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                placed += 1
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                placed += 1
            if placed >= n:
                return True
        return False