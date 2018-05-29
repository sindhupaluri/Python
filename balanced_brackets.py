# Write a function that accepts a string consisting entirely of brackets ([](){}) and returns whether it is balanced.
# Every "opening" bracket must be followed by a closing bracket of the same type.
# There can also be nested brackets, which adhere to the same rule.

# f('()[]{}(([])){[()][]}') // true
# f('())[]{}') // false
# f('[(])') // false


bracket_str = '())[]{}'
closing_braces = [']', '}', ')']
opening_braces = ['[', '{', '(']

open_close_map = {
    '}': '{',
    ']': '[',
    ')': '('
}

open_list = []
is_balanced = True

for i in bracket_str:
    if i in opening_braces:
        open_list.append(i)
    else:
        if len(open_list) == 0:
            is_balanced = False
            break

        k = open_list[-1]

        if k != open_close_map[i]:
            is_balanced = False
            break
        else:
            del open_list[-1]

if is_balanced:
    print("Balanced")
else:
    print("Not balanced")
