# Please write a program which counts and returns the numbers of each character in a string input.

# count_characters( "abcdegabc" )
# { 'a':2, 'c':2, 'b':2, 'e':1, 'd':1, 'g':1 }


def count_characters(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count)


count_characters("abcdegabc")
