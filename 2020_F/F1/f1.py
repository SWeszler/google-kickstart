def solution_bf(N, X, queue):
    res = []

    i = 0
    while len(res) < N:
        if queue[i] > 0:
            queue[i] -= X
            if queue[i] <= 0:
                res.append(str(i + 1))
                queue[i] = 0
        i += 1
        if i >= N:
            i = 0

    return " ".join(res)

def solution(N, X, queue):
    m = {i: n//X + (n % X > 0) for i, n in enumerate(queue)}
    m = sorted(m.items(), key=lambda item: item[1])
    return " ".join([str(i + 1) for i, v in m])


tc = int(input())
for i in range(1, tc + 1):
    N, X = input().split()
    queue = [int(p) for p in input().split()]
    out = solution(int(N), int(X), queue)
    print("Case #{}: {}".format(i, out))