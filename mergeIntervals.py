# Time Complexity: O(nlogn)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        new_arr = [intervals[0]]
        for curr in intervals[1:]:
            prev = new_arr[-1]
            if prev[1] >= curr[0]:
                if prev[1] <= curr[1]:
                    new_arr[-1] = [prev[0], curr[1]]
                else:
                    new_arr[-1] = prev
            else:
                new_arr.append(curr)
        return new_arr