def reverse_string(string):
    #Establish stack
    reverse_stack = []
    #Go through each character in the string to be reversed, 
    #adding each one to the stack
    for char in string:
        reverse_stack.append(char)

    #Establish a string to store the newly reversed string
    reversed_string = ""

    for _ in range(len(reverse_stack)):
        #Remove each letter and add it to the end of the reversed string
        reversed_string += reverse_stack.pop()
    return reversed_string

#Testing
assert reverse_string("hi there") == "ereht ih"
assert reverse_string("reverse string") == "gnirts esrever"
assert reverse_string("You can do this!") == "!siht od nac uoY"
print("Testing successful!")