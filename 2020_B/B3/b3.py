def matching_parentheses(input):
    """Returns pairs of indices for all matching parentheses 
    or None if at least one doesn't have a match"""
    stack = []
    res = {}
   
    for i, c in enumerate(input):
        if c == '(':
            stack.append(i)
            res[i] = 0
        elif c == ')':
            if not stack:
                return None
            opening = stack.pop()
            res[opening] = i

    if stack:
        return None
   
    return res


def solution_bf(P):
    brackets = matching_parentheses(P)
    w, h = 10**9 + 1, 10**9 + 1

    def helper(s, program=''):
        i = 0
        while i < len(s):
            if s[i] in 'NSEW':
                program += s[i]
                i += 1
            else:
                program += int(s[i]) * helper(s[i + 2: brackets[i + 1]])
                i = brackets[i + 1] + 1
        
        return program

    program = helper(P)

    for c in program:
        if c == 'N':
            h -= 1
        elif c == 'S':
            h += 1
        elif c == 'E':
            w += 1
        elif c == 'W':
            w -= 1

    w = w % 10**9
    h = h % 10**9

    return f'{w} {h}'


solution = solution_bf


tc = int(input())
for i in range(1, tc + 1):
    P = input()
    if i not in range(1,5):
        continue
    out = solution(P)
    print("Case #{}: {}".format(i, out))