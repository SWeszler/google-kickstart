def solution(N, K, S):
    spent = K - 1
    restart = spent + N + 1
    goback = spent + (K - S) + (N - S + 1)

    print(spent, N + 1, K - S, N - S + 1, restart, goback)

    return min(restart, goback)

tc = int(raw_input())
for i in xrange(1, tc + 1):
    N, K, S = raw_input().split()
    out = solution(int(N), int(K), int(S))
    print("Case #{}: {}".format(i, out))