# Python program for implementation of Quicksort

# This implementation uses the last element as the pivot.
# It maintains a pointer to track elements smaller than the pivot.
# At the end of the partition() function, the pivot is swapped with the element at the pointer position
# to achieve a "sorted" array relative to the pivot.

# Function to find the partition position
def partition(array, low_index, high_index):
    # Choose the rightmost element as the pivot
    pivot_value = array[high_index]

    # Pointer for the greater element
    smaller_element_index = low_index - 1

    # Traverse through all elements and compare each with the pivot
    for current_index in range(low_index, high_index):
        if array[current_index] <= pivot_value:
            # If an element smaller than the pivot is found,
            # increment the pointer for the smaller element
            smaller_element_index += 1

            # Swap the current element with the element at the smaller_element_index
            (array[smaller_element_index], array[current_index]) = (array[current_index], array[smaller_element_index])

    # Swap the pivot element with the element at the smaller_element_index + 1
    (array[smaller_element_index + 1], array[high_index]) = (array[high_index], array[smaller_element_index + 1])

    # Return the position from where partition is done
    return smaller_element_index + 1

# Function to perform quicksort
def quickSort(array, low_index, high_index):
    if low_index < high_index:
        # Find the pivot element such that elements smaller than the pivot are on the left
        # and elements greater than the pivot are on the right
        partition_index = partition(array, low_index, high_index)

        # Recursive call on the left of the pivot
        quickSort(array, low_index, partition_index - 1)

        # Recursive call on the right of the pivot
        quickSort(array, partition_index + 1, high_index)

# Sample data to be sorted
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array:")
print(data)

# Get the size of the data
size = len(data)

# Call the quickSort function to sort the data
quickSort(data, 0, size - 1)

# Print the sorted data
print('Sorted Array in Ascending Order:')
print(data)
