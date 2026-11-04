def is_balanced(expression: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False

    return len(stack) == 0


# Example usage:
expr = "{[()()]}"
print("Balanced:", is_balanced(expr))  # Output: True