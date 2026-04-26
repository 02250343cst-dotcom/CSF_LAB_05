stack = []
def push(item):
    stack.append(item)
def pop():
    if stack:
        return stack.pop()
    return "Stack is empty"
def peek():
    if stack:
        return stack[-1]
    return "Stack is empty"
# Testing
push(10)
push(20)
push(30)
print("Stack:", stack)
print("Top element:", peek())
print("Popped:", pop())
print("After pop:", stack)