def day_name(day_number):
    # Define a list of day names where the index corresponds to the day number
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # Check if the provided day_number is a valid index for the days list
    if 0 <= day_number <= 6:
        return days[day_number]
    else:
        # Return None for any invalid input
        return None

# Example Usage
print(day_name(0))  # Output: Sunday
print(day_name(3))  # Output: Wednesday
print(day_name(6))  # Output: Saturday
print(day_name(7))  # Output: None (invalid input)
