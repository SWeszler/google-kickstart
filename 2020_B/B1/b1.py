
def solution(N, points):
    res = 0
    for i in range(1, N - 1):
        if points[i - 1] < points[i] and points[i] > points[i + 1]:
            res += 1
    return res


tc = int(input())
for i in range(1, tc + 1):
    N = input()
    points = [int(p) for p in input().split()]
    out = solution(int(N), points)
    print("Case #{}: {}".format(i, out))