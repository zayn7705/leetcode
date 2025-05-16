# Time Complexity: O(n)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            width = r - l
            h = min(height[l], height[r])
            if width * h > max_area:
                max_area = width * h
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area