# Write a program to find if a given number is prime or not

number = 97
is_prime = True
for i in range(2, number):
    if number % i == 0:
        print("It is not a prime")
        is_prime = False
        break

if is_prime:
    print("It is a prime")
