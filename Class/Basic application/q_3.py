class Bracket:
    @staticmethod
    def is_valid_parenthesis(str1):
        stack, p_char = [], {"(": ")", "{": "}", "[": "]"}
        for parenthesis in str1:
            if parenthesis in p_char:
                stack.append(parenthesis)
            elif len(stack) == 0 or p_char[stack.pop()] != parenthesis:
                return False
        return len(stack) == 0


print(Bracket().is_valid_parenthesis("(){}[]"))
print(Bracket().is_valid_parenthesis("()[{)}"))
print(Bracket().is_valid_parenthesis("()"))
