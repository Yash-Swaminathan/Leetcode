class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        SortS = {}
        SortT = {}

        if len(s) != len(t):
            return False

        for i in range (len(s)):
            SortS[s[i]] = 1 + SortS.get(s[i], 0)
            SortT[t[i]] = 1 + SortT.get(t[i], 0)
        
        for c in SortS:
            if SortS[c] != SortT.get(c, 0):
                return False

        return True


# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

