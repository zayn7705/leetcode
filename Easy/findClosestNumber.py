# Time Complexity: O(n)
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        for i in nums:
            if (abs(i) < abs(min)) or (abs(i) == abs(min) and i > min):
                min = i
        return min