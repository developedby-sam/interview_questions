# 49. Group Anagrams
# Medium

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


from collections import defaultdict

# TIME COMPLEXITY --> O(m*n)
def groupAnagrams(strs):
    # Dictionary to store anagram groups
    anagram_groups = defaultdict(list)

    for word in strs:
        # For storing the count of every char
        count = [0] * 26  # a ... z

        # 1. Calculate the index by converting the char to its ascii value
        # 2. Ex. ASCII(a) --> 97 & ASCII(b) = 98 --> index of b == 1
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        # Store the results in the dictionary
        # Key --> list of count of every char in a word
        # Convert key into tuple rather than list
        # Since keys cannot be mutable type (list --> mutable) && (tuple --> immutable)
        anagram_groups[tuple(count)].append(word)
    
    # Return only the values
    # Since the values are the list of anagrams
    return [*anagram_groups.values()]


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        