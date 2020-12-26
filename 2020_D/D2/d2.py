
def solution_mem(K, notes):
    dp = {}
    def findMin(start, i):

        if (start, i) in dp:
            return dp[start, i]

        if i < 0:
            return K

        min_val = findMin(start, i - 1)

        down, up = 1, 5
        if 0 < i < K:
            if notes[i] > notes[i - 1]:
                down = start + 1
                up = 5
            elif notes[i] < notes[i - 1]:
                down = 1
                up = start

        breaks = 1
        if down >= up:
            breaks = 0
            down, up = 1, 5

        for c in range(down, up):
            min_val = min(min_val, findMin(c, i - 1) - breaks)

        dp[start, i] = min_val
        return min_val
    
    mn = K
    for c in range(1, 5):
        mn = min(mn, findMin(c, K - 1))
    return mn


def solution_1(K, notes):
    dp = [[K for j in range(5)] for i in range(K)]

    for i in range(K):
        for j in range(1, 5):
            breaks = 0
            down, up = 1, 5
            start = j
            for _ in range(min(i)):
                if i > 0:
                    if notes[i] > notes[i - 1]:
                        down = start + 1
                        up = 5
                        start += 1
                    elif notes[i] < notes[i - 1]:
                        down = 1
                        up = start
                        start -= 1
                if down >= up:
                    breaks = 1
                    down, up = 1, 5
                    start = j
                
            print('breaks:', breaks, j, i, notes[i])

            dp[i][j] = min(dp[i][j], dp[i - 1][j] + breaks - 1)

    for r in dp:
        print(r)
    return dp[-1][-1]


def solution(K, notes):
    dp = [[K for j in range(4)] for i in range(K)]

    for j in range(4):
        dp[0][j] = 0

    for i in range(1, K):
        for jp in range(4):
            for j in range(4):
                violation = 1
                if (notes[i] > notes[i - 1] and j > jp) or (notes[i] < notes[i - 1] and j < jp) or (notes[i] == notes[i - 1] and j == jp):
                    violation = 0
                dp[i][j] = min(dp[i][j], dp[i - 1][jp] + violation)

    return min(dp[-1])


tc = int(input())
for i in range(1, tc + 1):
    K = input()
    notes = [int(p) for p in input().split()]
    out = solution(int(K), notes)
    print("Case #{}: {}".format(i, out))