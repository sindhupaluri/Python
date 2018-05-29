# all_unique("python") # > True
# all_unique("Smart lady.") # > False


def all_unique(string):
    char_count = {}
    is_unique = True

    for i in string:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
        if char_count[i] > 1:
            is_unique = False
            break

    if is_unique:
        print("{} is unique".format(string))
    else:
        print("{} is not unique".format(string))


all_unique("Smart lady")
