from typing import List

pair = {
    '}': '{',
    ')': '(',
    ']': '['
}


def is_correct_bracket_seq(bracket_seq: List[str]) -> bool:
    s = list(bracket_seq)
    stack = list()
    for i in s:
        if i == '{' or i == '(' or i == '[':
            stack.append(i)
        elif (i in pair) and (len(stack) != 0) and (pair[i] == stack[-1]):
            stack.pop()
        else:
            return False
    if len(stack) != 0:
        return False
    else:
        return True

seq = list(input().strip())
print(is_correct_bracket_seq(seq))
