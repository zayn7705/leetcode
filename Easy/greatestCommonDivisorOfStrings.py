# Time complexity: O(n * m)
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        small = ""
        big = ""
        if len(str1) <= len(str2):
            small = str1
            big = str2
        else:
            small = str2
            big = str1
        for i in range(len(small), 0, -1):
            if len(small) % i == 0:
                x = small[0:i]
                if x * (len(small) // i) == small and len(big) % i == 0 and x * (len(big) // i) == big:
                    return x
        return ""
