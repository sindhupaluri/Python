# Write a program to construct two dimensional array and print the same

lst1 = []
for j in range(1, 4):
    lst2 = []
    for i in range(1, 6):
        lst2.append(i)

    lst1.append(lst2)

for k in lst1:
    for l in k:
        print(l, end=' ')
    print()
