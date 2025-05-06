# Time complexity: O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lMult = 1
        rMult = 1
        
        lArr = [0] * len(nums)
        rArr = [0] * len(nums)
        
        for i in range(len(nums)):
            j = -i - 1
            lArr[i] = lMult
            rArr[j] = rMult
            lMult *= nums[i]
            rMult *= nums[j]
        return [l * r for l, r in zip(lArr, rArr)]