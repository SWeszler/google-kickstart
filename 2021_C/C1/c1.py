
def solution_bf(N, K, s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = 0

    strings = ['']
    for n in range(N):
        new_str = []
        for x in strings:
            for y in alphabet[:K]:
                cand = x + y                
                new_str.append(cand)
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
    
solution = solution_bf

tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    s = input()
    out = solution(int(N), int(K), s)
    print("Case #{}: {}".format(i, out))
