# Time Complexity: O(n^2)
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        if len(candies) <= 1:
            return [True]
        most = -1
        arr = []
        for num in candies:
            if num > most:
                most = num
        for num in candies:
            if num + extraCandies >= most:
                arr.append(True)
            else:
                arr.append(False)
        return arr