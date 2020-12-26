
def solution(P):
    a = 10**9
    dp = {
        'N': 0,
        'S': 0,
        'E': 0,
        'W': 0
    }

    def helper(s):
        mul = 1
        for c in s:
            if c in '1234567890':
                mul = int(c)

    return a


tc = int(input())
for i in range(1, tc + 1):
    P = input()
    # if i != 3:
    #     continue
    out = solution(P)
    print("Case #{}: {}".format(i, out))