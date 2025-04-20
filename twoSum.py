# Intuition:
# My first thought is to check all possible pairs of numbers and see if any pair adds up to the target.

# Approach:
# I use a brute-force approach with two nested loops. The outer loop picks the 
# first number and the inner loop checks every other number after it. 
# If the sum of the pair equals the target, I return their indices. 
# The condition `i != j` is technically redundant due to how the loops are structured,
# but it reinforces the requirement that the two indices must be different.

# Complexity:
# Time complexity: O(n^2)
# Because we check every pair of elements in the list using nested loops.

# Space complexity: O(1)
# We're not using any extra space beyond a few variables.

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target and i != j):
                    return [i, j]
