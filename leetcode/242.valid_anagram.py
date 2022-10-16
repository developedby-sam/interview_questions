# 242. Valid Anagram
# Easy

# 7222

# 240

# Add to List

# Share
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

###################################################
############## S O L U T I O N ####################
###################################################

def isAnagram(s: str, t: str):

    # Solution 1
    # return sorted(s) == sorted(t)
    
    # If length is not same s & t can never be anagram
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    # count the occurance of every letter in both the strings
    # and store it in hash maps
    for indx in range(len(s)):
        count_s[s[indx]] = 1 + count_s.get(s[indx], 0)
        count_t[t[indx]] = 1 + count_t.get(t[indx], 0)

    # Determine anagram or not based on the counts of the letter
    # sotred in the hash maps
    for count in count_s:
        if count_s[count] != count_t.get(count, 0):
            return False
    return True


print(isAnagram('anagram', 'nagaram'))