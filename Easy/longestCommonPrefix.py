# Time Complexity: O(n * m)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = float('inf')
        out = ""
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        i = 0
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return out
            out += strs[0][i]
            i += 1
        return out