
def solution_bf(N, K, s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = 0

    strings = ['']
    for n in range(N):
        new_str = []
        for x in strings:
            for y in alphabet[:K]:
                new_str.append(x + y)
        strings = new_str

    def is_smaller(s1, s2):
        p1 = 0
        p2 = 0
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            else:
                return s1[p1] < s2[p2]

    for st in strings:
        if is_smaller(st, s) and st == st[::-1]:
            res += 1

    return res % (10**9 + 7)


def solution_optimal(N, K, s):
    alphabet = {c: ord(c) - 97 for c in 'abcdefghijklmnopqrstuvwxyz'}
    H = -(-N // 2)
    max_res = 10**9 + 7
    res = 0

    def pow(base, exp, mod):
        res = 1
        base %= mod
        if base == 0:
            return 0
        while exp > 0:
            if exp & 1 == 1:
                res = (res * base) % mod
            exp >>= 1
            base = (base * base) % mod

        return res

    for i in range(H):
        res += alphabet[s[i]] * pow(K, H - i - 1, max_res)

    def is_smaller(s1, s2):
        p1 = 0
        p2 = 0
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
            else:
                return s1[p1] < s2[p2]

    s1 = s[:H]
    if is_smaller(s1[::-1], s[H - (len(s) % 2):]):
        res += 1

    return res % max_res


solution = solution_optimal

tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    s = input()
    out = solution(int(N), int(K), s)
    print("Case #{}: {}".format(i, out))
