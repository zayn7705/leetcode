# Time complexity: O(n)
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []

        for char in s:
            if stack and stack [-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            if stack[-1][1] == k:
                stack.pop()
        
        final_s = ""
        for char, count in stack:
            final_s += char * count
        return final_s