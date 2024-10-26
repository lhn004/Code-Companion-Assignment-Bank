# First solution:
# Prompt the user for input
user_input = input("Enter a sentence or phrase: ")

# Replace each space in the input with three periods
modified_output = user_input.replace(' ', '...')

# Print the modified string
print(modified_output)


# Second solution:
# Prompt the user for input
user_input = input("Please enter your text: ")

# Initialize an empty string to build the output
output = ""

# Iterate through each character in the user input
for char in user_input:
    if char == ' ':  # Check if the character is a space
        output += '...'  # Add three periods to the output
    else:
        output += char  # Otherwise, add the character itself

# Print the modified output
print(output)

