# Write a program to print the longest length string from given input list of strings.

list_of_strings = ["America", "India", "Paris", "Germany", "Australia"]
output = ''
temp = 0

for i in list_of_strings:
    count = len(i)
    if count > temp:
        temp = count
        output = i

print(output)

