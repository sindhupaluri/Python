# Given an integer array, output all distinct pairs that sum up to a specific value k.
# Consider the fact that the same number can add up to k with its duplicates in the array.

# Example
# f(10, [3, 4, 5, 6, 7]) // [ [4, 6], [3, 7] ]
# f(8, [3, 4, 5, 4, 4]) // [ [3, 5], [4, 4], [4, 4], [4, 4] ]
# f(10, [3, 5, 6, 8]) // []

input_sum = 10
input_array = [3, 4, 5, 6, 7]

for index, i in enumerate(input_array):
    for indx, j in enumerate(input_array):
        if indx <= index:
            continue
        if i + j == input_sum:
            print(i, j)
