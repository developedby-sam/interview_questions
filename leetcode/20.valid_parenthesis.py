# TIME COMPLEXITY O(N) & SPACE COMPLEXITY O(N)
def valid_parenthesis(string):

    # Mappings of closed and opened parenthesis
    close_to_open_map = {
        ")": '(',
        "}": '{',
        "]": "["
    }

    stack = []

    for char in string:
        # If char is closed parenthesis
        # check if stack has matching opened parenthesis or not
        # empty stack means string is starting with closed parenthesis which is invalid
        if char in close_to_open_map:
            
            # If matching open parenthesis is at the top of the stack 
            # means matching open parenthesis is present at a valid location
            if stack and stack[-1] == close_to_open_map[char]:
                stack.pop()
            else:

                # If matching open parenthesis is not found
                # the string has invalid parenthesis sequences
                return False
        else:
            # If char is open parenthesis append it to the stack
            stack.append(char)

    # All valid matching parenthesis are found only if the stack is empty at the end --> return True
    # else unmatching parenthesis are present in the stack --> return False
    return True if not stack else False

print(valid_parenthesis('(){()}'))