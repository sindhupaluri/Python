# The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two
# Write a function that accepts a number and returns the number at that position in the fibonnaci sequence.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

fibonacci_num = 10
num1 = 0
num2 = 1
total = 0

while total < fibonacci_num:
    print(num1, end=' , ')
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    total += 1
