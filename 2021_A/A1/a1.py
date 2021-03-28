
def solution(N, K, s):
    p1 = 0
    p2 = N - 1
    mid = N // 2

    diff = 0
    while p1 <= mid and p2 >= mid:
        if s[p1] != s[p2]:
            diff += 1

        p1 += 1
        p2 -= 1

    return abs(K - diff)


tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    s = input()
    out = solution(int(N), int(K), s)
    print("Case #{}: {}".format(i, out))
