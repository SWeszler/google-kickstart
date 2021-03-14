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

    def helper(i, j, total):
        key = "{}{}{}".format(i, j, total)
        if key in dp:
            return dp[key]

        res = 0

        if i == H and j == W:
            return total

        if U <= i <= D and L <= j <= R:
            return 0
        
        if i == H:
            res += helper(i, j + 1, total)
        elif j == W:
            res += helper(i + 1, j, total)
        else:
            total *= 0.5
            res += helper(i + 1, j, total)
            res += helper(i, j + 1, total)

        dp[key] = res
        return res

    return helper(1, 1, 1)



solution = solution_dp

tc = input()

for i in range(1, int(tc) + 1):
    W, H, L, U, R, D = raw_input().split()
    out = solution(int(W), int(H), int(L), int(U), int(R), int(D))
    print("Case #{}: {}".format(i, out))