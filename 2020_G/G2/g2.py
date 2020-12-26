def solution(N, m):
    dp = [[0 for j in range(N + 1)] for i in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i < N and j < N:
                m[i][j] += m[i - 1][j - 1]
            dp[i][j] = max(m[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


tc = int(input())
for i in range(1, tc + 1):
    N = int(input())
    m = []
    for n in range(N):
        m.append([int(j) for j in input().split()])
    out = solution(N, m)
    print("Case #{}: {}".format(i, out))