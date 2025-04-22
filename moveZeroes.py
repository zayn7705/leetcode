# Time complexity: O(n)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        counter = 0
        for i in nums:
            if i != 0:
                nums[counter] = i
                counter += 1
        while counter < len(nums):
            nums[counter] = 0
            counter += 1