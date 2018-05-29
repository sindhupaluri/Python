# Reverse a given input list.

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = []
for index, i in enumerate(lst1):
    lst2 = [i] + lst2

print(lst2)
