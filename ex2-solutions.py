def count_substring(main_string, substring):
    # Initialize a counter to keep track of occurrences
    count = 0
    
    # Calculate the length of the substring
    sub_len = len(substring)
    
    # Iterate over the main string to check for the substring
    for i in range(len(main_string) - sub_len + 1):
        # Check if the substring from current index matches the target substring
        if main_string[i:i + sub_len] == substring:
            count += 1  # Increment count if a match is found
    
    # Return the total count of occurrences
    return count

# Example Usage
print(count_substring("hello world", "o"))  # Output: 2
print(count_substring("hello hello hello", "hello"))  # Output: 3
print(count_substring("abcabcabc", "abc"))  # Output: 3
print(count_substring("ababab", "aba"))  # Output: 2
