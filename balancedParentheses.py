# Imports the "Stack" class from "stack.py"
from stack import Stack

# Function to check if two(2) characters represent an opening and closing pair of parentheses
def check_if_matching(c1, c2):

    # Checks if the two characters represent a matching pair of parentheses
    if c1 == "(" and c2 == ")":

        # Returns true to indicate that the two chars match
        return True
    
    # Checks if the two characters represent a matching pair of curly braces
    elif c1 == "{" and c2 == "}":

        # Returns true to indicate that the two chars match
        return True

    # Checks if the two characters represent a matching pair of square brackets
    elif c1 == "[" and c2 == "]":

        # Returns true to indicate that the two chars match
        return True

    # If the two characters don't represent a matching pair of parentheses
    else:
        
        # Returns false to indicate that the two chars don't match
        return False

# Function to determine if the parentheses are balanced in a given string
def check_if_parentheses_are_balanced(inString):

    # Declares an instance of the Stack class
    s = Stack()

    # Boolean flag variable to indicate if the string has balanced parentheses
    # Initialized to true
    balanced_flag = True

    # Variable to keep track of the index of the current character being evaluated
    index = 0

    # Loop to continue while:
    # The current character index is less than the length of the specified string &
    # The parentheses are still considered balanced
    while index < len(inString) and balanced_flag:

        # Stores the character stored that the current index
        current_character = inString[index]

        # Checks if the current character being evaluated is an open parentheses variant
        if current_character in "([{":

            # Adds the current character to the top of the stack
            s.push(current_character)

        # Checks if:
        # The current character is not an opening parenthesis variant &
        # The stack is current empty
        # Accounts for the case that there are no opening parentheses
        elif s.checkIfEmpty():

            # Indicates that the parentheses in the string are not balanced
            balanced_flag = False

        else:

            # Stores the top element of the stack
            top = s.pop()

            # Checks if the two characters represent a pair of opening and closing parentheses
            # Compares the innermost parentheses pair that has yet to be evaluated
            if check_if_matching(top, current_character) == False:

                # Indicates that the parentheses in the string are not balanced
                balanced_flag = False

        
        # Increments the index to evaluate the next character in the string
        index += 1

    # Checks if:
    # The stack is in fact empty &
    # The parentheses are still considered balanced
    if s.checkIfEmpty() and balanced_flag:

        # Returns true to indicate that the string contains balanced pairs of parentheses
        return True

    # If either of the conditions are not met
    else:

        # Returns false to indicate that the string of parentheses is not balanced
        return False

# Defines five(5) strings to be evaluated
string1 = "(((({}))))"
string2 = "[][]]]"
string3 = "[][]"
string4 = "[({})]"
string5 = "[)][(]"

# Displays the title of this program
print("\nDetermining if strings of parentheses are balanced:")

# Checks if the strings of parentheses are balanced and outputs the result
print("\nThe first string: " + string1 + " is balanced (T/F): " + str(check_if_parentheses_are_balanced(string1)))
print("\nThe second string: " + string2 + " is balanced (T/F): " + str(check_if_parentheses_are_balanced(string2)))
print("\nThe third string: " + string3 + " is balanced (T/F): " + str(check_if_parentheses_are_balanced(string3)))
print("\nThe fourth string: " + string4 + " is balanced (T/F): " + str(check_if_parentheses_are_balanced(string4)))
print("\nThe fifth string: " + string5 + " is balanced (T/F): " + str(check_if_parentheses_are_balanced(string5)))


            

