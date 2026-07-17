# Group Anagrams
# Medium
# Topics
# Company Tags
# Hints
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:


# "act":[act,act]
# "pots":[pots,tops,stop]
# "hat":[hat]


# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.
"""
U - 
"""

class Solution:
    def groupAnagrams(self, strs):
        hash_map = {
        }
        if len(strs) == 0:
            return [strs]
        for str in strs:
            var = "".join(sorted(str))
            hash_map.setdefault(var,[]).append(str)
        return [hash_map[key] for key in hash_map]

s1 = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
# strs = [""]
print(s1.groupAnagrams(strs=strs))
    
        