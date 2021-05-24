def solution(N, K, strings):
    pass


tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    strings = []
    for j in range(int(N)):
        strings.append(input())

    out = solution(int(N), int(K), strings)
    print("Case #{}: {}".format(i, out))