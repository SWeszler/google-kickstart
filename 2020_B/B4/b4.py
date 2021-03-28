#https://www.youtube.com/watch?v=fpnNaAU0iPk&list=PLmdFyQYShrjfPLdHQxuNWvh2ct666Na3z&index=15

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
    """ TODO - fix some issues with floating point """
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
    from math import log, exp
    res = 0

    def prob(log_fac, n, k):
        return exp(log_fac[n] - log_fac[k] - log_fac[n - k] - n * log(2))

    log_fac = [0.0]
    for x in range(1, W + H - 2):
        log_fac.append(log_fac[-1] + log(x))

    x = L - 1
    y = D + 1
    while y <= H and x > 0:
        n = x + y - 2
        k = x - 1
        res += prob(log_fac, n, k) if y < H else prob(log_fac, n - 1, k) / 2.0
        if y < H:
            y += 1
        x -= 1

    x = R + 1
    y = U - 1
    while x <= W and y > 0:
        n = x + y - 2
        k = y - 1
        res += prob(log_fac, n, k) if x < W else prob(log_fac, n - 1, k) / 2.0
        if x < W:
            x += 1
        y -= 1

    return res


solution = solution_optimal

tc = input()
for i in range(1, int(tc) + 1):
    W, H, L, U, R, D = input().split()
    out = solution(int(W), int(H), int(L), int(U), int(R), int(D))
    print(f"Case #{i}: {out}")