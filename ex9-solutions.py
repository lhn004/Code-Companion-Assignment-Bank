def bubble_sort(values):
    n = len(values)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
    return values
