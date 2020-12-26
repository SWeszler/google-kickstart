
def solution(N, K, integers):
    res = 0
    count = 0

    for i in range(N - 1):
        if integers[i] == K:
            count += 1

        if count > 0 and integers[i] == (integers[i + 1] + 1):
            count += 1
        else:
            count = 0

        if count == K:
            res += 1
            count = 0

    return res


tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    integers = [int(p) for p in input().split()]
    out = solution(int(N), int(K), integers)
    print("Case #{}: {}".format(i, out))