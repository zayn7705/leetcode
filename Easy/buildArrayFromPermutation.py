# Time complexity: O(n)
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(0, len(nums)):
            ans.append(nums[nums[i]])
        return ans