def binary_search(values, target):
  # Initialize the starting index of the search area
  left = 0
  # Initialize the ending index of the search area
  right = len(values) - 1

   # Keep searching while the search area has at least one element
  while left <= right:
      # Calculate the middle index of the search area
      mid = (left + right) // 2

      # Check if the target is at the middle index
      if values[mid] == target:
          # Target found, return its index
          return mid
      # If the target is greater than the middle element,
      # it must be in the right half of the search area
      elif values[mid] < target:
          left = mid + 1
      # If the target is less than the middle element,
      # it must be in the left half of the search area
      else:
          right = mid - 1
        
  # If we exit the loop, the target was not found
  return -1

