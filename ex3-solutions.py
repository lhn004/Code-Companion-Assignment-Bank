def remove_first_occurrence_manual(main_string, substring):
    # Lengths of the main string and the substring
    main_len = len(main_string)
    sub_len = len(substring)
    
    # Check if the substring length is greater than the main string length
    if sub_len > main_len:
        return main_string

    # Loop through the main string to find the substring
    for i in range(main_len - sub_len + 1):
        # Check the current part of the main string against the substring
        if main_string[i:i + sub_len] == substring:
            # If found, return the string before and after the substring
            return main_string[:i] + main_string[i + sub_len:]
    
    # If the substring is not found, return the original string
    return main_string

# Example Usage
print(remove_first_occurrence_manual("hello world", "world"))  # Output: "hello "
print(remove_first_occurrence_manual("hello hello", "hello"))  # Output: " hello"
print(remove_first_occurrence_manual("hello world", "test"))   # Output: "hello world"
print(remove_first_occurrence_manual("the quick brown fox", "quick "))  # Output: "the brown fox"
