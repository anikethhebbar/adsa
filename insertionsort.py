def insertion_sort(array):
    # Calculate the length of the array
    array_length = len(array)
    
    # If the array has 0 or 1 element, it is already sorted, so return
    if array_length <= 1:
        return

    # Iterate over the array starting from the second element (index 1)
    for current_index in range(1, array_length):
        # Store the current element as the value to be inserted in the right position
        current_value = array[current_index]
        # Initialize the previous index to the element before the current one
        previous_index = current_index - 1

        # Move elements that are greater than current_value one position ahead
        while previous_index >= 0 and current_value < array[previous_index]:
            # Shift elements to the right to make space for the current_value
            array[previous_index + 1] = array[previous_index]
            # Move to the previous element
            previous_index -= 1

        # Insert the current_value in the correct position
        array[previous_index + 1] = current_value

# Get user input for the array to be sorted
array_to_sort = []

# Number of elements as input
n = int(input("Enter number of elements: "))

# Iterating till the range
for i in range(n):
    ele = int(input())
    # Adding the element
    array_to_sort.append(ele)

# Call the insertion_sort function to sort the array
insertion_sort(array_to_sort)

# Print the sorted array
print(array_to_sort)
