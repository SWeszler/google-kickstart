
def solution(N, A, B, C):
    cb = [N for i in range(C)]
    ab = []
    bb = []

    i = N - (A - C)
    for _ in range(A - C):
        ab.append(i)
        i += 1

    i = N - 1
    for _ in range(B - C):
        bb.append(i)
        i -= 1

    res = ab + cb + bb

    i = 1
    while len(res) < N and i < len(res):
        if res[i] > 1 and res[i - 1] > 1:
            res[:] = res[:i] + [1]*(N - len(res)) + res[i:]
        else:
            i += 1

    if len(res) != N:
        return "IMPOSSIBLE"

    return " ".join([str(n) for n in res])


tc = int(input())
for i in range(1, tc + 1):
    N, A, B, C = input().split()
    out = solution(int(N), int(A), int(B), int(C))
    print("Case #{}: {}".format(i, out))