def check_balance(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0
 
test1 = "(a+b)*(c+d)"
test2 = "(a+b)*(c+d"
test3 = "{[()]}"
 
print(f"{test1}: {'Balanced' if check_balance(test1) else 'Not Balanced'}")
print(f"{test2}: {'Balanced' if check_balance(test2) else 'Not Balanced'}")
print(f"{test3}: {'Balanced' if check_balance(test3) else 'Not Balanced'}")
 