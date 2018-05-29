# Convert all the vowels to uppercase for the given input string.

new_string = "aeroplane"
vowels = {'a', 'i', 'e', 'o', 'u'}

for i in new_string:
    if i in vowels:
        new_string = new_string.replace(i, i.upper())

print(new_string)
