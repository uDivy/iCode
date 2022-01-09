# Solution 1
def balancedBrackets(string):
    # Write your code here.
    left_par = ['(','{','[']
    right_par = [')','}',']']
    stack = []
    for b in string:
        if b in left_par:
            stack.append(b)
        elif b in right_par:
            if len(stack):
                if stack[-1] == left_par[right_par.index(b)]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        else:
            continue

    return False if len(stack) else True

# Solution 2 O/p true instead of false
# failed for
# {
#   "string": "{[[[[({(}))]]]]}"
# }
def balancedBrackets(string):
    # Write your code here.
    left_par = ['(', '{', '[']
    right_par = [')', '}', ']']
    stack = []


    for b in string:
        if b in left_par:
            stack.append(b)
        elif b in right_par:
            if len(stack):
                print('f', stack)
                sub_stack = []
                if b == ')':
                    a = stack.pop()
                    while a != '(' and len(stack) != 0:
                        sub_stack.append(a)
                        a = stack.pop()
                    stack.extend(sub_stack)

                elif b == ']':
                    a = stack.pop()
                    while a != '[' and len(stack) != 0:
                        sub_stack.append(a)
                        a = stack.pop()
                    stack.extend(sub_stack)

                elif b == '}':
                    a = stack.pop()
                    while a != '{' and len(stack) != 0:
                        sub_stack.append(a)
                        a = stack.pop()
                    stack.extend(sub_stack)

            else:
                print(stack)
                return False
        else:
            continue
    print("l", stack)
    return False if len(stack) else True