def solution(N, A):
    res = 0
    dp = [1, 2] + [0 for i in range(N - 2)]
    repl = -1
    diff = abs(A[1] - A[0])
    count = 2

    for i in range(2, N):
        if abs(A[i] - A[i - 1]) == diff:
            count += 1
        elif repl < 0:
            count += 1
            repl = i
            A[i] = A[i - 1] + abs(A[i - 1] - A[i - 2])
        else:
            dp[i] = max(i - repl, dp[i - 1])
            diff = abs(A[i] - A[i - 1])
            count = 1

        dp[i] = max(dp[i - 1], count)

    res = dp[-1]

    dp = [0 for i in range(N - 2)] + [2, 1]
    repl = -1
    diff = abs(A[-1] - A[-2])
    count = 2
        
    for i in range(N - 2, -1, -1):
        if abs(A[i] - A[i + 1]) == diff:
            count += 1
        elif repl < 0:
            count += 1
            repl = i
            A[i] = A[i + 1] + abs(A[i + 1] - A[i + 2])
        else:
            dp[i] = max(repl - i, dp[i + 1])
            diff = abs(A[i] - A[i + 1])
            count = 1

        dp[i] = max(dp[i + 1], count)

    return max(dp[-1], res)


def solution_bf(N, A):
    if N <= 2:
        return 2

    res = 0
    for i in range(1, N):
        diff = A[i] - A[i - 1]
        A1 = A[:]
        count = 1
        fix = 1
        for j in range(i, N):
            if diff == A1[j] - A1[j - 1]:
                count += 1
            elif fix <= 0:
                break
            else:
                count += 1
                fix -= 1
                A1[j] = A1[j - 1] + diff
        
        count += fix
        count = N if count > N else count
        res = max(count, res)

        if i < N - 2:
            diff = (A[i + 1] - A[i - 1]) // 2
            A1 = A[:]
            count = 1
            fix = 1
            for j in range(i, N):
                if diff == A1[j] - A1[j - 1]:
                    count += 1
                elif fix <= 0:
                    break
                else:
                    count += 1
                    fix -= 1
                    A1[j] = A1[j - 1] + diff
            
            res = max(res, count)

    return res


solution = solution_bf


tc = int(input())
for i in range(1, tc + 1):
    N = input()
    A = [int(a) for a in input().split()]
    out = solution(int(N), A)
    print("Case #{}: {}".format(i, out))