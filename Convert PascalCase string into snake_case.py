'''
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

Examples
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
'''
##
'''
def to_underscore(string):
    a=list(string)
    for i in range(1,len(a)):
        if a[i].islower():
            continue
        else:
            a.insert(i,'_')
    s=''.join(a)
    s=s.lower() 
    return s
'''
def to_underscore(string):
    # Check if the input is a string
    if not isinstance(string, str):
        return str(string)  # Return the input unchanged if it's not a string
    
    # Initialize an empty list to store the converted characters
    converted = []
    
    # Iterate over each character in the string
    for i, char in enumerate(string):
        # Check if the character is uppercase and not the first character
        if char.isupper() and i > 0:
            # Check if the previous character is not an underscore
            if string[i - 1] != '_':
                # Add an underscore before the uppercase letter
                converted.append('_')
            # Convert the uppercase letter to lowercase and add it
            converted.append(char.lower())
        else:
            # Add the character as is
            converted.append(char)
    
    s=''.join(converted)
    s=s.lower()
    # Convert the list of characters back to a string and return it
    return s


