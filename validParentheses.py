def is_valid(s):
    brackets = { '{': '}', '(': ')', '[': ']' }
    stack = []

    is_open = False

    if len(s) < 0 and len(s)%2 != 0 and s[0] not in brackets:
        return False

    for c in s:
        if c in brackets:
            is_open = True
            stack.append(c)
        elif len(stack) > 0 and c == brackets[stack[-1]]:
            stack.pop()
            if len(stack) == 0:
                is_open = False
        else:
            return False

    if is_open:
        return False
                
    return True


strs = input('')
result = is_valid(strs)
print(result)

# valid:  ()  ()[]{}  ([])   
# invalid:  (]  ([)]  (){}}{

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.