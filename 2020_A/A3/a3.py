def solution_set1(N, K, M):
    D = []

    for i in range(1, len(M)):
        d = M[i] - M[i - 1]
        D.append(d)

    D.sort(reverse=True)
    D[0] =  -(-D[0] // 2)
    
    return max(D)


def solution_optimal(N, K, M):
    m = 0
    D = []

    for i in range(1, len(M)):
        d = M[i] - M[i - 1]
        D.append(d)
        m = max(m, d)

    l = 1
    r = m
    res = None

    while l <= r:
        mid = (l + r) // 2
        ksum = 0
        for d in D:
            ksum += -(-d // mid) - 1

        if ksum <= K:
            res = mid
            r = mid - 1
        else:
            l = mid + 1

    return res

        
solution = solution_optimal

tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    M = [int(p) for p in input().split()]
    out = solution(int(N), int(K), M)
    print("Case #{}: {}".format(i, out))