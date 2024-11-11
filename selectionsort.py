# Selection sort in Python
# Time complexity: O(n*n)
# Sorting by finding the minimum element and swapping it with the first unsorted element

def selection_sort(array, array_size):
    # Traverse through all array elements
    for current_index in range(array_size):
        # Find the minimum element in the remaining unsorted array
        min_index = current_index

        # Iterate through the unsorted elements
        for next_index in range(current_index + 1, array_size):
            # Select the minimum element in every iteration
            if array[next_index] < array[min_index]:
                min_index = next_index
        
        # Swap the found minimum element with the first unsorted element
        (array[current_index], array[min_index]) = (array[min_index], array[current_index])

# Sample array to be sorted
sample_array = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
# Get the size of the array
sample_array.sort()
# array_size = len(sample_array)
# # Call the selection_sort function to sort the array
# selection_sort(sample_array, array_size)
# # Print the sorted array
print('The array after sorting in Ascending Order by selection sort is:')
print(sample_array)
