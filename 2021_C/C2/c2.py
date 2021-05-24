def solution(G):
    res = 0

    for i in range(1, G + 1):
        s = 0
        k = i
        while s <= G:
            s += k
            k += 1
            if s == G:
                res += 1

    return res


tc = int(input())
for i in range(1, tc + 1):
    G = input()
    out = solution(int(G))
    print("Case #{}: {}".format(i, out))