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
    w, h = 1, 1

    def helper(l, r):
        i = l
        program = ''
        while i < r:
            if P[i] in 'NSEW':
                program += P[i]
                i += 1
            else:
                program += int(P[i]) * helper(i + 2, brackets[i + 1])
                i = brackets[i + 1] + 1
        
        return program

    program = helper(0, len(P))

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

    w = 10**9 if w == 0 else w
    h = 10**9 if h == 0 else h

    return f'{w} {h}'


def solution_low_memory(P):
    brackets = matching_parentheses(P)

    def helper(l, r):
        i = l
        w, h = 0, 0
        while i < r:
            if P[i] == 'N':
                h -= 1
                i += 1
            elif P[i] == 'S':
                h += 1
                i += 1
            elif P[i] == 'E':
                w += 1
                i += 1
            elif P[i] == 'W':
                w -= 1
                i += 1
            else:
                w1, h1 = helper(i + 2, brackets[i + 1])
                w += int(P[i]) * w1
                h += int(P[i]) * h1
                i = brackets[i + 1] + 1
        
        return w, h

    w, h = helper(0, len(P))

    w = (w + 1) % 10**9
    h = (h + 1) % 10**9

    w = 10**9 if w == 0 else w
    h = 10**9 if h == 0 else h

    return f'{w} {h}'


solution = solution_low_memory


tc = int(input())
for i in range(1, tc + 1):
    P = input()
    out = solution(P)
    print("Case #{}: {}".format(i, out))