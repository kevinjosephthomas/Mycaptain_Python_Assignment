def most_frequent(s):
    # Create an empty dictionary
    char_frequency = {}
    
    # Iterate through each character in the string
    for char in s:
        # If the character is already in the dictionary, increment its frequency
        if char in char_frequency:
            char_frequency[char] += 1
        # Otherwise, add the character to the dictionary with a frequency of 1
        else:
            char_frequency[char] = 1
    
    # Sort the dictionary by frequency in descending order
    sorted_char_frequency = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Print the characters in order of frequency
    for char, frequency in sorted_char_frequency:
        print(char, end='')

# Take input from the user
input_string = input("Enter a string: ")

# Call the function with the input string
most_frequent(input_string)
