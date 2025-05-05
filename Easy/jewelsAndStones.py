# Time complexity: O(n * m)
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        if len(stones) <= 0:
            return 0
        s = set(jewels)
        count = 0
        for stone in stones:
            if stone in s:
                count += 1
        return count