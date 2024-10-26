# First solution:
# Prompt the user for a greeting
user_input = input("Enter your greeting: ")

# Remove leading and trailing whitespaces manually
trimmed_input = ""
start = 0
end = len(user_input)

# Strip leading whitespace
while start < end and user_input[start] == ' ':
    start += 1

# Strip trailing whitespace
while end > start and user_input[end - 1] == ' ':
    end -= 1

trimmed_input = user_input[start:end].lower()  # Extract the trimmed part and convert to lower case

# Determine the output based on the greeting
if trimmed_input[:5] == "hello":  # Check if the greeting starts with 'hello'
    print("$0")
elif trimmed_input[:1] == "h":    # Check if the greeting starts with 'h'
    print("$20")
else:
    print("$100")


#Second solution:
# Prompt the user for a greeting
user_input = input("Enter your greeting: ")

# Strip any leading whitespace and convert the string to lower case for uniformity
normalized_input = user_input.strip().lower()

# Check the conditions for the greeting
if normalized_input.startswith("hello"):
    # If the greeting starts exactly with "hello"
    print("$0")
elif normalized_input.startswith("h"):
    # If the greeting starts with "h" but not "hello"
    print("$20")
else:
    # If the greeting doesn't start with "h"
    print("$100")
