# Time Complexity: O(n + m)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mergedWord = ""
        minLen = min(len(word1), len(word2))

        for i in range(minLen):
            mergedWord += word1[i]
            mergedWord += word2[i]
        
        mergedWord += word1[minLen:] + word2[minLen:]

        return mergedWord
        