def solution(N, K, M):
    return 0




tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    M = [int(p) for p in input().split()]
    out = solution(int(N), int(K), M)
    print("Case #{}: {}".format(i, out))