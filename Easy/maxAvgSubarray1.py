# Time Complexity: O(n)
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        tot = sum(nums[:k])
        big_tot = tot
        for j in range(k, len(nums)):
            tot += nums[j] - nums[j - k]
            big_tot = max(big_tot, tot)
        return float(big_tot) / k