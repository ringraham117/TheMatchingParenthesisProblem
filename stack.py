# Defining the "Stack" class
class Stack:

    # Constructor for the Stack class
    def __init__(self):

        # Declares a list to represen the stack elements
        self.elements = [] 

    # Function to add an element to the top of the stack
    # "Push onto the top"
    def push(self, item):

        # Adds the specified element to the end of the list of elements
        self.elements.append(item)

    # Function to remove the top element from the stack and return its value
    # "Pop off of the top"
    def pop(self):

        # Removes the last element of the list and returns its value
        return self.elements.pop()

    # Function to check if the stack is empty
    def checkIfEmpty(self):

        # Returns true if the list of elements is an empty list
        # Else, returns false
        return self.elements == []

    # Function to return the top value of the stack
    def peek(self):

        # Checks if the stack contains any elements ("Not empty")
        if self.checkIfEmpty() != True:

            # Returns the LAST element in the list
            # Negative indices can be used to index from the end of a list
            return self.elements[-1]

    # Function to return a list of the elements in the stack
    def getStackElements(self):

        # Returns the list of stack elements
        return self.elements

    