# 125. Valid Palindrome
# Easy

# 5140

# 6170

# Add to List

# Share
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# TIME COMPLEXITY O(N)
def valid_palindrome(string):
    new_string = ''

    for char in string:
        if char.isalnum():
            new_string += char.lower()

    return new_string == new_string[::-1]


def valid_palindrome_2(string):
    left, right = 0, len(string) -1

    # check unles left pointer croses right pointer
    # meaning until every char of string is not checked
    while left < right:

        # increase left pointer if char at left index is not alpha numeric
        # insure that left pointer does not croses right pointer
        while left < right and not is_alnum(string[left]):
            left += 1

        # decreament right pointer if char at right index is not alpha numeric
        # insure that right pointer does not croses left pointer
        while right > left and not is_alnum(string[right]):
            right -= 1

        # if char at left and right pointer does not matched
        # string is not palindrome
        if string[left].lower() != string[right].lower():
            return False
        
        left, right = left + 1, right - 1

    return True

# Helper function to check if char is alpha numeric
def is_alnum(char):
    return (
        ord('A') <= ord(char) <= ord('Z') or
        ord('a') <= ord(char) <= ord('z') or
        ord('0') <= ord(char) <= ord('9')
    )

print(valid_palindrome_2('A man, a plan, a canal: Panama'))