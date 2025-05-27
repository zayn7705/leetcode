# Time Complexity: O(n)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_max = nums[0]
        prev_min = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        ans = nums[0]

        for i in nums[1:]:
            curr_max = max(max(prev_max * i, prev_min * i), i)
            curr_min = min(min(prev_max * i, prev_min * i), i)
            prev_max = curr_max
            prev_min = curr_min
            ans = max(ans, curr_max)
        return ans