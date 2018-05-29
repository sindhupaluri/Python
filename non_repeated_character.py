# Write a function that accepts a single string input and returns the first non-repeated character.

# "AABBC" // "C"
# "AABBCCDEEFF" // "D"


string = "AABBC"
dct = {}

for i in string:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

for j in dct:
    if dct[j] == 1:
        print(j)


