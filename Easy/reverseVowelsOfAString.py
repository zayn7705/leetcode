# Time complexity: O(n)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        validVowels = set("aeiouAEIOU")
        s_list = list(s)
        vowels = []
        vowelPos = []

        for i in range(len(s_list)):
            if s_list[i] in validVowels:
                vowels.append(s_list[i])
                vowelPos.append(i)

        for i in range(len(vowelPos)):
            s_list[vowelPos[i]] = vowels.pop()

        return "".join(s_list)