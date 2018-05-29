# Write a program to find the factorial of a given number
# factorial of 5 is 5 x 4 x 3 x 2 x 1


number = 5
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print(factorial)

