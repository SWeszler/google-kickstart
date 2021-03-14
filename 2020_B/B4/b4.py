def gen_paths(i, j, stack):
    if (i == H and j == W):
        print(stack + [[i, j]])
        return

    stack.append([i, j])
    if i == H:
        gen_paths(i, j + 1, stack)
    elif j == W:
        gen_paths(i + 1, j, stack)
    else:
        gen_paths(i + 1, j, stack)
        gen_paths(i, j + 1, stack)
    stack.pop()



def solution_bf(W, H, L, U, R, D):
    probs = []

    def helper(i, j, total):
        if i == H and j == W:
            probs.append(total)
            return
        if U <= i <= D and L <= j <= R:
            return
        
        if i == H:
            helper(i, j + 1, total)
        elif j == W:
            helper(i + 1, j, total)
        else:
            total *= 0.5
            helper(i + 1, j, total)
            helper(i, j + 1, total)

    helper(1, 1, 1)

    return sum(probs)


def solution_dp(W, H, L, U, R, D):
    dp = {}

    def helper(i, j):
        key = f"{i}{j}"
        if key in dp:
            return dp[key]

        res = 0.0
        if i == H and j == W:
            return 1

        if U <= i <= D and L <= j <= R:
            return 0.0
        
        if i == H:
            res += helper(i, j + 1)
        elif j == W:
            res += helper(i + 1, j)
        else:
            res += 0.5 * helper(i + 1, j) + 0.5 * helper(i, j + 1)

        dp[key] = res
        return res

    res = helper(1, 1)
    return res


def solution_optimal(W, H, L, U, R, D):
    from math import factorial
    X = []
    Y = []
    res = 0

    def get_x(i, j):
        if not 1 <= i <= H or not 1 <= j <= W:
            return
        X.append([i, j])
        get_x(i + 1, j - 1)

    def get_y(i, j):
        if not 1 <= i <= H or not 1 <= j <= W:
            return
        Y.append([i, j])
        get_y(i - 1, j + 1)

    get_x(D + 1, L - 1)
    get_y(U - 1, R + 1)

    for x in X:
        x_prob = 0.5**(L + D - 2)
        x_paths = factorial(x[0] + x[1] - 2) / (factorial(x[1] - 1) * factorial(x[0] - 1))
        res += x_prob * x_paths

    for y in Y:
        y_prob = 0.5**(R + U - 2)
        y_paths = factorial(y[0] + y[1] - 2) / (factorial(y[1] - 1) * factorial(y[0] - 1))
        res += y_prob * y_paths

    return res



solution = solution_optimal

tc = input()
for i in range(1, int(tc) + 1):
    W, H, L, U, R, D = input().split()
    # if i != 1:
    #     continue
    out = solution(int(W), int(H), int(L), int(U), int(R), int(D))
    print(f"Case #{i}: {out}")