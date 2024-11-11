def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    # n starts from the end of the list and decreases to 1
    for n in range(len(arr) - 1, 0, -1):
        # Inner loop to compare adjacent elements
        # i goes from the start of the list to n-1
        for i in range(n):
            # If the current element is greater than the next element
            if arr[i] > arr[i + 1]:
                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Sample list to be sorted
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

# Call the bubble_sort function to sort the list
bubble_sort(arr)

# Print the sorted list
print("Sorted list is:")
print(arr)